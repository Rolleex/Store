from django import forms

productitem_quantity_choices = [(i, str(i)) for i in range(1, 21)]


class CartAddForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=productitem_quantity_choices, coerce=int, empty_value=1, label='Кол-Во')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
