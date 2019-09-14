from django import forms
from django.forms import ModelForm
from .models import Afectiuni, StatiuniBalneare

class AdaugareAfectiuniForm(ModelForm):
    class Meta:
        model = Afectiuni
        fields = ('clasificare', 'DecontatCNAS')

class StatiuniBalneareForm(ModelForm):
    class Meta:
        model = StatiuniBalneare
        fields = ('nume', 'judet')
