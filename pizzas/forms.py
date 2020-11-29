from django import forms
from .models import *

class PizzaForm(forms.ModelForm):

    class Meta:
        model = Pizza
        fields = ['name', 'pizza_img']