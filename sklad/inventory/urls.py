from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('login/', views.org_login, name='org_login'),
    path('logout/', views.org_logout, name='org_logout'),
    path('', views.product_list, name='product_list'),
]
