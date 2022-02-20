from django import views
from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    path('lista/', views.ListAllEmpleados.as_view(), name='employee_all'),
    path('list-admin/', views.ListAllEmpleadosAdmin.as_view(),
         name='employee_all_admin'),
    path('list-by-area/<shortname>',
         views.ListByArea.as_view(), name='employees_by_area'),
    path('list-by-skill/', views.ListBySkill.as_view(), name='employees_by_skill'),
    path('list-by-job/<job>', views.ListByJob.as_view(), name='employees_by_job'),
    path('find-employee', views.ListByKword.as_view(), name='employees_by_kword'),
    path('detail-employee/<pk>', views.EmpleadoDetailView.as_view(),
         name='detail_employee'),
    path('create-employee/', views.EmpleadoCreateView.as_view(),
         name='create_employee'),
    path('create-skill/', views.SkillCreateView.as_view(), name='create_skill'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('update-employee/<pk>/', views.EmpleadoUpdateView.as_view(),
         name='modificar_empleado'),
    path('delete-employee/<pk>/', views.EmpleadoDeleteView.as_view(),
         name='eliminar_empleado'),
]
