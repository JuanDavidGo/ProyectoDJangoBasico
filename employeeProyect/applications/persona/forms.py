import imp
from tkinter import Widget
from django import forms

from .models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = (
            'first_name', 
            'last_name', 
            'job', 
            'departamento', 
            'skills',
            'avatar'
        )
        widgets = {
            'first_name' : forms.TextInput(
                attrs= {
                    'placeholder' : 'Nombres'
                }
            ),
            'skills' : forms.CheckboxSelectMultiple()
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name.isdigit():
            raise forms.ValidationError('Solo se permiten letras')
        
        return first_name
