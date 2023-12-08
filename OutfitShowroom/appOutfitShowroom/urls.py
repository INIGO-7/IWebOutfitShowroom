from django.urls import path
from . import views

urlpatterns = [
    # '' vacío será el por defecto
    # el name es muy importante para hacer vínculos entre las páginas
    path('', views.index, name='pagina_principal'),
    path('ocasiones', views.ocasiones, name='ocasiones'),
    path('estilos', views.estilos, name='estilos'),
    path('outfits', views.outfits, name='outfits'),
    path('contactos', views.contactos, name='contactos'),
    path('outfit/<int:outfit_id>', views.detalle_outfit, name='detalle_outfit'),
    path('ocasion/<int:ocasion_id>', views.detalle_ocasion, name='detalle_ocasion'),
    path('estilo/<int:estilo_id>', views.detalle_estilo, name='detalle_estilo')
]