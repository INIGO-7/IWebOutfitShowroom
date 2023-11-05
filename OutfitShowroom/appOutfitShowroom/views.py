from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Outfit, Estilo, Ocasion, Outfit
from django.http import HttpResponse

#TODO: PONER BONITO CON TEMPLATES DE HTML, ABAJO ESTA COMO DEBERÍA QUEDAR
# EL CÓDIGO CUANDO TENGAMOS LAS PLANTILLAS

def index(request):
	outfits = Outfit.objects.order_by('nombre')
	output = ", ".join([o.nombre for o in outfits])
	return HttpResponse(output)

#devuelve los datos de un outfit
def detail(request, outfit_id):
	outfit = Outfit.objects.get(pk=outfit_id)
	return HttpResponse(outfit)

# #devuelve el listado de outfits
# def index_outfits(request):
# 	outfits = get_list_or_404(Outfit.objects.order_by('nombre'))
# 	context = {'lista_outfits': outfits }
# 	return render(request, 'index.html', context)

# #devuelve los datos de un outfit
# def show_outfit(request, outfit_id):
# 	outfit = get_object_or_404(Outfit, pk=outfit_id)
# 	context = {'outfit': outfit }
# 	return render(request, 'detail.html', context)

# #devuelve el listado de estilos
# def index_estilos(request):
# 	estilos = get_list_or_404(Estilo.objects.order_by('nombre'))
# 	context = {'lista_estilos': estilos }
# 	return render(request, 'index.html', context)

# #devuelve los datos de un estilo
# def show_estilo(request, estilo_id):
# 	estilo = get_object_or_404(Estilo, pk=estilo_id)
# 	context = {'estilo': estilo }
# 	return render(request, 'detail.html', context)

# #devuelve el listado de ocasiones
# def index_ocasiones(request):
# 	ocasiones = get_list_or_404(Ocasion.objects.order_by('nombre'))
# 	context = {'lista_ocasiones': ocasiones }
# 	return render(request, 'index.html', context)

# #devuelve los datos de una ocasion
# def show_ocasion(request, ocasion_id):
# 	ocasion = get_object_or_404(Ocasion, pk=ocasion_id)
# 	context = {'ocasion': ocasion }
# 	return render(request, 'detail.html', context)