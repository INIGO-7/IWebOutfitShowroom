from django.urls import path
from . import views

urlpatterns = [
    # '' vacío será el por defecto
    # el name es muy importante para hacer vínculos entre las páginas
    path('', views.Index.as_view(), name='pagina_principal'),
    path('ocasiones', views.OcasionListView.as_view(), name='ocasiones'),
    path('estilos', views.EstiloListView.as_view(), name='estilos'),
    path('outfits', views.OutfitListView.as_view(), name='outfits'),
    path('contactos', views.contactos, name='contactos'),
    path('outfit/<int:pk>', views.OutfitDetailView.as_view(), name='detalle_outfit'),
    path('ocasion/<int:pk>', views.OcasionDetailView.as_view(), name='detalle_ocasion'),
    path('estilo/<int:pk>', views.EstiloDetailView.as_view(), name='detalle_estilo')
]