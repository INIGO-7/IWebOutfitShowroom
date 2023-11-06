from django.urls import path
from . import views

urlpatterns = [
    # '' vacío será el por defecto
    # el name es muy importante para hacer vínculos entre las páginas
    path('', views.index, name='index'),
    path('ocasiones', views.lista_ocasiones, name='lista_ocasiones'),
    path('estilos', views.lista_estilos, name='lista_estilos'),
    path('outfits', views.lista_outfits, name='lista_outfits'),
    path('outfit/<int:outfit_id>', views.outfit, name='outfit'),
    path('ocasion/<int:ocasion_id>', views.ocasion, name='ocasiones'),
    path('estilo/<int:estilo_id>', views.estilo, name='estilo')
]