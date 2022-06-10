from errno import EDESTADDRREQ
from django import forms
from .models import EquationValues

class AddEquationValues(forms.ModelForm):
    class Meta:
        model = EquationValues
        fields = ['a', 'b', 'c']