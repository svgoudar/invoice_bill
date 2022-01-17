from django.forms import ModelForm, TextInput, NumberInput, ChoiceField, CharField,ModelChoiceField,MultipleChoiceField,ModelMultipleChoiceField
from .models import items
from django import forms
from django.core.exceptions import ValidationError



class purchaseForm(ModelForm):

    class Meta:
        model = items
        fields = ["item", "item_category", "quantity", "price"]

        labels = {'item': 'Item', 'item_category': 'Item Category', 'quantity': 'Quantity of item',
                  'price': "The price of Item"}
        widgets = {'item': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the item'}),
                   'quantity': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the number of item'}),
                   'price': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the cost of item'}),
                   }

   
