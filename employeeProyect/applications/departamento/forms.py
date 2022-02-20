from django import forms

from .models import Departamento

class DepartamentoForm(forms.Form):

    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento =  forms.CharField(max_length=50)
    shortname = forms.CharField(max_length=20)
    
    class Meta:
        model = Departamento
        fields = (
            'name',
            'short_name',
            'anulate'
        )
        widgets = {
            'first_name' : forms.TextInput(
                attrs= {
                    'placeholder' : 'Nombres'
                }
            ) 
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name.isdigit():
            raise forms.ValidationError('Solo se permiten letras')
        
        return first_name
