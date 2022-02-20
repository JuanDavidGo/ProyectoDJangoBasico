from django.shortcuts import render
from django.views.generic.edit import (
    FormView
)
from django.views.generic import (
    ListView,
)

from .forms import DepartamentoForm

from .models import Departamento
from applications.persona.models import Empleado

# Create your views here.


class DepartamentoCreateView(FormView):
    form_class = DepartamentoForm
    template_name = "departamento/create_departamento.html"
    success_url = "persona/lista"

    def form_valid(self, form):

        departamento = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['shortname']
        )

        departamento.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=departamento
        )
        return super(DepartamentoCreateView, self).form_valid(form)


class ListAllDepartamentos(ListView):
    template_name = 'departamento/list_all.html'
    model = Departamento
    context_object_name = 'departamentos'
