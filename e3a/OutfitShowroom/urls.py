"""
URL configuration for OutfitShowroom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #estos nombres son los dominios del proyecto, al poner http://127.0.0.1:8000/nombredominio
    #el primer path es vacio, esto es porque lleva a http://127.0.0.1:8000, sin nombre de dominio de una página adicional
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include('appOutfitShowroom.urls')),
    #path("admin/", admin.site.urls),
]
