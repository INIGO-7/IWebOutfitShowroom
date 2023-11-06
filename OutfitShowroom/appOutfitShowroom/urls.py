from django.urls import path
from . import views

urlpatterns = [
    # '' vacío será el por defecto
    # el name es muy importante para hacer vínculos entre las páginas
    path('', views.index, name='index'),
    path('ocasiones', views.lista_ocasiones, name='lista_ocasiones'),
    path('estilos', views.lista_estilos, name='lista_estilos'),
    path('outfits', views.lista_outfits, name='lista_outfits'),
    path('outfit/<int:outfit_id>', views.detail, name='detail')
]