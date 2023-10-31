from django.urls import path
from . import views

urlpatterns = [
    # '' vacío será el por defecto
    # el name es muy importante para hacer vínculos entre las páginas
    path('', views.index_departamentos, name='index'),
    path('departamentos/<int:departamento_id>/', views.show_departamento, name='detail'),
    path('departamentos/<int:departamento_id>/empleados', views.index_empleados, name='empleados'),
    path('empleados/<int:empleado_id>', views.show_empleado, name='empleado'),
    path('habilidades/<int:habilidad_id>', views.show_habilidad, name='habilidad'),
]
