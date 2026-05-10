from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count, Sum, Q, F
from .models import Product, Category, Organization
from .forms import OrganizationLoginForm


def org_login(request):
    if not request.user.is_authenticated:
        from django.contrib.auth.views import LoginView
        return LoginView.as_view(template_name='inventory/django_login.html')(request)

    if request.session.get('organization_id'):
        return redirect('inventory:product_list')

    if request.method == 'POST':
        form = OrganizationLoginForm(request.POST)
        if form.is_valid():
            org = form.cleaned_data['organization']
            request.session['organization_id'] = org.id
            request.session['organization_name'] = org.name
            messages.success(request, f'Вы вошли: {org.name}')
            return redirect('inventory:product_list')
    else:
        form = OrganizationLoginForm()

    return render(request, 'inventory/login.html', {'form': form})


def org_logout(request):
    request.session.pop('organization_id', None)
    request.session.pop('organization_name', None)
    messages.info(request, 'Вы вышли')
    return redirect('inventory:org_login')


def product_list(request):
    if not request.user.is_authenticated or not request.session.get('organization_id'):
        return redirect('inventory:org_login')

    org_id = request.session['organization_id']
    products = Product.objects.filter(organization_id=org_id)
    categories = Category.objects.filter(organization_id=org_id)

    if cat_id := request.GET.get('category'):
        products = products.filter(category_id=cat_id)

    if search := request.GET.get('q'):
        products = products.filter(name__icontains=search) | products.filter(sku__icontains=search)

    stats = products.aggregate(
        low_stock=Count('id', filter=Q(quantity__gt=0, quantity__lte=F('min_limit'))),
        out_of_stock=Count('id', filter=Q(quantity=0)),
        total_value=Sum(F('price') * F('quantity'))
    )

    return render(request, 'inventory/product_list.html', {
        'products': products,
        'categories': categories,
        'low_stock_count': stats['low_stock'] or 0,
        'out_of_stock_count': stats['out_of_stock'] or 0,
        'total_value': stats['total_value'] or 0,
    })
