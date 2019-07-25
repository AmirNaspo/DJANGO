from django.forms import ModelForm
from .models import *
from django.forms.widgets import ClearableFileInput
from django import forms

class empregadoForm(ModelForm):
    #Foto = forms.ImageField(widget=ClearableFileInput)
    class Meta:
        model = empregado
        fields = ['Nome','Area', 'Observacoes', 'Foto']

class ProfileForm (ModelForm):
    class Meta:
        model = Profile
        fields = ['user','Area','Nome', 'Observacoes', 'Foto']
#class id (ModelForm):
 #   class Meta:
  #      model = id
   #     fields = ['ID_func', 'ID_atv', 'Data']
class pontForm (ModelForm):
    class Meta:
        model = pont
        fields = ['ColdCall','LALA']