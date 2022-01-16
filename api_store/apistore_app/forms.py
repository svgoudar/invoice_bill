from django.forms import ModelForm, TextInput, NumberInput, ChoiceField, CharField,ModelChoiceField,MultipleChoiceField,ModelMultipleChoiceField
from .models import items
from django import forms
from django.core.exceptions import ValidationError

# class textchoices(forms.ChoiceField):
tax = {'Medicine': 5, 'Food': 5, 'Music': 3, 'Total': 5, 'Imported': 18}

choices = ((5, "Medicine")
           , (5, "Food"),
           (3, "Music"),
           (18, "Imported"),
           (0, "Book"))


class purchaseForm(ModelForm):
    # choice_category = forms.ChoiceField(choices=choices)

    class Meta:
        model = items
        fields = ["item", "item_category", "quantity", "price"]

        labels = {'item': 'Item', 'item_category': 'Item Category', 'quantity': 'Quantity of item',
                  'price': "The price of Item"}
        widgets = {'item': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the item'}),
                   'quantity': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the number of item'}),
                   'price': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the cost of item'}),
                   }

    # def clean(self):
    #     raise ValidationError("Do not enter duplicate value")
