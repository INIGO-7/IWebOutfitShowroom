from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Outfit, Estilo, Ocasion, Outfit
from django.http import HttpResponse
from django.db.models import Max


def index(request):

	# Get the latest outfit date for each ocasion
	ultimas_fechas_outfits = Outfit.objects.values('ocasion').annotate(latest_date=Max('fecha'))

	# Now, get the latest outfit for each ocasion
	ultimos_outfits_porocasion = []
	for outfit_date in ultimas_fechas_outfits:
		latest_outfit = Outfit.objects.filter(ocasion=outfit_date['ocasion'], fecha=outfit_date['latest_date']).first()
		if latest_outfit:
			ultimos_outfits_porocasion.append(latest_outfit)
	
	context = {'titulo_pagina': "Inicio", 'ultimos_outfits': ultimos_outfits_porocasion}
	return render(request, 'index.html', context)

def lista_ocasiones(request):
	ocasiones = Ocasion.objects.all()
	context = {'titulo_pagina': "Ocasiones", 'ocasiones': ocasiones}
	return render(request, 'ocasiones.html', context)

def lista_estilos(request):
	estilos = Estilo.objects.all()
	context = {'titulo_pagina': "Estilos", 'estilos': estilos}
	return render(request, 'estilos.html', context)

def lista_outfits(request):
	outfits = Outfit.objects.all()
	context = {'titulo_pagina': "Outfits", 'outfits': outfits}
	return render(request, 'outfits.html', context)

#devuelve los datos de un outfit, ocasion o estilo

def detalles_estilo(request, estilo_id):
	estilo = Estilo.objects.get(pk=estilo_id)
	outfits = Outfit.objects.filter(estilo=estilo_id)
	context = {'titulo_pagina': "Detalles del estilo", 'estilo': estilo, 'outfits': outfits}
	return render(request, 'estilo.html', context)

def detalles_ocasion(request, ocasion_id):
	ocasion = Ocasion.objects.get(pk=ocasion_id)
	outfits = Outfit.objects.filter(ocasion=ocasion_id)
	context = {'titulo_pagina': "Detalles de la ocasión", 'ocasion': ocasion, 'outfits': outfits}
	return render(request, 'ocasion.html', context)

def detalles_outfit(request, outfit_id):
	outfit = Outfit.objects.get(pk=outfit_id)
	ocasion = Ocasion.objects.get(pk=outfit_id)
	estilos = Estilo.objects.filter(outfit=outfit_id)
	context = {'titulo_pagina': "Detalles del outfit", 'outfit': outfit,  'ocasion': ocasion, 'estilos': estilos}
	return render(request, 'outfit.html', context)