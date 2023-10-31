from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Departamento, Habilidad, Empleado

#devuelve el listado de empresas
def index_departamentos(request):
	departamentos = get_list_or_404(Departamento.objects.order_by('nombre'))
	context = {'lista_departamentos': departamentos }
	return render(request, 'index.html', context)

#devuelve los datos de un departamento
def show_departamento(request, departamento_id):
	departamento = get_object_or_404(Departamento, pk=departamento_id)
	context = {'departamento': departamento }
	return render(request, 'detail.html', context)

#devuelve los empelados de un departamento
def index_empleados(request, departamento_id):
	departamento = get_object_or_404(Departamento, pk=departamento_id)
	empleados =  departamento.empleado_set.all()
	context = {'departamento': departamento, 'empleados' : empleados }
	return render(request, 'empleados.html', context)

#devuelve los detalles de un empleado
def show_empleado(request, empleado_id):
	empleado = get_object_or_404(Empleado, pk=empleado_id)
	habilidades =  empleado.habilidades.all()
	context = { 'empleado': empleado, 'habilidades' : habilidades }
	return render(request, 'empleado.html', context)

# Devuelve los detalles de una habilidad
def show_habilidad(request, habilidad_id):
    habilidad = get_object_or_404(Habilidad, pk=habilidad_id)
    empleados =  habilidad.empleado_set.all()
    context = { 'empleados': empleados, 'habilidad' : habilidad }
    return render(request, 'habilidad.html', context)