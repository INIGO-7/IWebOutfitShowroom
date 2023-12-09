from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Outfit, Estilo, Ocasion, Contacto
from django.http import HttpResponse, Http404
from django.db.models import Max
from django.core.serializers import serialize
import json


def index(request):

	# Obtiene los outfits mas recientemente añadidos por ocasion
	ultimos_outfits = (
		Outfit.objects.raw('SELECT * FROM( SELECT * FROM appOutfitShowroom_Outfit ORDER BY fecha DESC) GROUP BY ocasion_id ')
	)

	context = {
		'titulo_pagina': "Inicio",
		'ultimos_outfits': ultimos_outfits
	}
	return render(request, 'index.html', context)

def ocasiones(request):
	ocasiones = get_list_or_404(Ocasion.objects.all())

	context = {
		'titulo_pagina': "Ocasiones",
		'ocasiones': ocasiones
	}
	return render(request, 'ocasiones.html', context)

def estilos(request):
	estilos = get_list_or_404(Estilo.objects.all())

	context = {
		'titulo_pagina': "Estilos",
		'estilos': estilos
	}
	return render(request, 'estilos.html', context)

def outfits(request):
	outfits = get_list_or_404(Outfit.objects.all())

	context = {
		'titulo_pagina': 'Outfits',
		'outfits': outfits
	}
	return render(request, 'outfits.html', context)

def contactos(request):
	contacts = get_list_or_404(Contacto.objects.all())

	data = serialize('json', contacts)
	data = json.loads(data)

	contacts_json = json.dumps([item['fields'] for item in data])

	context = {
		'titulo_pagina': 'Contactos',
		'contacts_json': contacts_json
	}

	return render(request, 'contactos.html', context)

#devuelve los datos de un outfit, ocasion o estilo

def detalle_estilo(request, estilo_id):
	estilo = get_object_or_404(Estilo, pk=estilo_id)

	context = {
		'titulo_pagina': "Detalles del estilo", 
		'estilo': estilo, 
		'outfits': estilo.outfit_set.all()
	}
	return render(request, 'estilo.html', context)

def detalle_ocasion(request, ocasion_id):
	ocasion = get_object_or_404(Ocasion, pk=ocasion_id)

	context = {
		'titulo_pagina': "Detalles de la ocasión",
		'ocasion': ocasion,
		'outfits': ocasion.outfit_set.all()
	}
	return render(request, 'ocasion.html', context)

def detalle_outfit(request, outfit_id):
	outfit = get_object_or_404(Outfit, pk=outfit_id)
	
	context = {
		'titulo_pagina': "Detalles del outfit",
		'outfit': outfit,
		'ocasion': outfit.ocasion,
		'estilos': outfit.estilos.all
	}
	return render(request, 'outfit.html', context)