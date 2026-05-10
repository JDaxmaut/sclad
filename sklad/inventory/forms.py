from django import forms
from .models import Organization


class OrganizationLoginForm(forms.Form):
    """Форма входа с выбором организации."""
    organization = forms.ModelChoiceField(
        queryset=Organization.objects.all(),
        label="Выберите организацию",
        widget=forms.Select(attrs={
            'class': 'org-select',
            'autofocus': True
        }),
        empty_label="--- Выберите из списка ---"
    )
