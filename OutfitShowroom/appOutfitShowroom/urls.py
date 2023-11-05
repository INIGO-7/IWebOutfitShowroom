from django.urls import path
from . import views

urlpatterns = [
    # '' vacío será el por defecto
    # el name es muy importante para hacer vínculos entre las páginas
    path('', views.index, name='index'),
    path('outfit/<int:outfit_id>', views.detail, name='detail')
]
