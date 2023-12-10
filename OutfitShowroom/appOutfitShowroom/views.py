from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import DetailView, ListView

from .models import Outfit, Estilo, Ocasion, Contacto
from django.http import HttpResponse, Http404
from django.db.models import Max
from django.core.serializers import serialize
import json


class Index(ListView):
    model = Outfit
    template_name = 'index.html'
    queryset = (
        Outfit.objects.raw(
            'SELECT * FROM( SELECT * FROM appOutfitShowroom_Outfit ORDER BY fecha DESC) GROUP BY ocasion_id ')
    )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Inicio'
        return context


class OcasionListView(ListView):
    model = Ocasion
    template_name = 'ocasiones.html'
    queryset = Ocasion.objects.all()

    def get_context_data(self, **kwargs):
        context = super(OcasionListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Ocasiones'
        return context


class EstiloListView(ListView):
    model = Estilo
    template_name = 'estilos.html'
    queryset = Estilo.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EstiloListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Estilos'
        return context

class OutfitListView(ListView):
    model = Outfit
    template_name = 'outfits.html'
    queryset = Outfit.objects.all()

    def get_context_data(self, **kwargs):
        context = super(OutfitListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Outfit'
        return context

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

# devuelve los datos de un outfit, ocasion o estilo

class EstiloDetailView(DetailView):
    model = Estilo
    template_name = "estilo.html"

    def get_context_data(self, **kwargs):
        context = super(EstiloDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del estilo'
        return context

class OcasionDetailView(DetailView):
    model = Ocasion
    template_name = "ocasion.html"

    def get_context_data(self, **kwargs):
        context = super(OcasionDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de la ocasion'
        return context

class OutfitDetailView(DetailView):
    model = Outfit
    template_name = "outfit.html"

    def get_context_data(self, **kwargs):
        context = super(OutfitDetailView, self).get_context_data(**kwargs)
        context["titulo_pagina"] = 'Detalles del outfit'
        return context
