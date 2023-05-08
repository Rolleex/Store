from django import forms
from .models import OrderModel


class OrderModelForms(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ['first_name', 'last_name', 'email', 'address', 'city']
        
