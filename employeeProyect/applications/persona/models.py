from django.db import models
from django.forms import CharField
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.

class Skills(models.Model):
    skill = models.CharField('Habilidad', max_length=50)

    class meta:
        verbose_name = 'Habilidad'
        verbose_name_prural = 'Habilidades Empleados'
    
    def __str__(self):
        return str(self.id) + '-' + self.skill

class Empleado(models.Model):

    JOB_CHOICES = (
    ('0', 'CONTADOR'),
    ('1', 'ADMINISTRADOR'),
    ('2', 'ECONOMISTA'),
    ('23', 'OTRO'),
    )

    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    full_name = models.CharField('Nombre completo', max_length=120, blank=True)
    job = models.CharField('Trabajo',choices=JOB_CHOICES, max_length=50)
    departamento = models.ForeignKey(Departamento, verbose_name="Departamento del empleado", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank = True, null = True)
    skills  = models.ManyToManyField(Skills)
    cv = RichTextField()

    class Meta:
        verbose_name = "Mi empleado"
        verbose_name_plural = "Empleados de la empresa"
        ordering = ['first_name']
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name