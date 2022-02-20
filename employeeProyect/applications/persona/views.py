
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
from .models import Empleado, Skills
from .forms import EmpleadoForm

class HomeView(TemplateView):
    template_name = 'home.html'

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'

    context_object_name = 'empleados'

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        print(kword)
        lista = Empleado.objects.filter(
            first_name__icontains=kword
        )
        return lista

class ListByArea(ListView):
    template_name = 'persona/list_by_area.html'
    def get_queryset(self):
        area = self.kwargs['shortname']
        
        lista = Empleado.objects.filter(
            departamento__short_name=area
        )
        return lista
    
    def get_context_data(self, **kwargs):
        area = self.kwargs['shortname']
        context = super(ListByArea, self).get_context_data(**kwargs)
        context['area'] = area
        return context

class ListByKword(ListView):
    template_name = 'persona/list_by_kword.html'

    context_object_name = 'empleados'
    
    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        print(kword)
        lista = Empleado.objects.filter(
            first_name__contains=kword
        )
        return lista

class ListBySkill(ListView):
    template_name = 'persona/list_by_skill.html'
    context_object_name = 'skills'

    def get_queryset(self):
        empleado = Empleado.objects.get(id='1')
        skills = empleado.skills.all()
        return skills

class ListByJob(ListView):
    template_name = 'persona/list_by_job.html'

    def get_queryset(self):
        job = self.kwargs['job']

        lista = Empleado.objects.filter(
            job = job
        )
        return lista

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context

class SuccessView(TemplateView):
    template_name = "persona/success.html"
    
class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "persona/create_empleado.html"
    success_url = reverse_lazy('persona_app:employee_all_admin')

    def form_valid(self, form):
        
        employee = form.save(commit=False)
        employee.full_name = employee.first_name + ' ' + employee.last_name
        employee.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class SkillCreateView(CreateView):
    model = Skills
    fields = ('__all__')
    template_name = "persona/create_skill.html"
    success_url = "."


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'departamento', 'skills']
    template_name = "persona/update.html"

    def get_success_url(self):
          pk=self.kwargs['pk']
          print(id)
          return reverse_lazy('persona_app:employee_all_admin')

    def post(self, request, *args, **kwargs):

        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        
        employee = form.save(commit=False)
        employee.full_name = employee.first_name + ' ' + employee.last_name
        employee.save()
        return super(EmpleadoUpdateView, self).form_valid(form)



class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:employee_all_admin')


class ListAllEmpleadosAdmin(ListView):
    template_name = 'persona/list_all_admin.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado
    