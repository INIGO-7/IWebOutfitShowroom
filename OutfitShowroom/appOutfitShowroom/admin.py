from django.contrib import admin
from .models import Estilo, Ocasion, Outfit

class EstiloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_en')
    search_fields = ('nombre', 'nombre_en')

class OcasionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_en')
    search_fields = ('nombre', 'nombre_en')

class OutfitAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'descripcion', 'precio', 'imagen')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('estilos', 'ocasion')



admin.site.register(Estilo, EstiloAdmin)
admin.site.register(Ocasion, OcasionAdmin)
admin.site.register(Outfit, OutfitAdmin)