from django.contrib import admin
from django.urls import path

from . import views

app_name = "departamento_app"

urlpatterns = [
    path('list-departamento/', views.ListAllDepartamentos.as_view(),
         name='list_departamentos'),
    path('create-department/', views.DepartamentoCreateView.as_view(),
         name='nuevo_departamento')
]
