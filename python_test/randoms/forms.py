from django import forms
from .models import Ball

class AddBallNumber(forms.ModelForm):
    class Meta:
        model = Ball
        fields = ['ball',]