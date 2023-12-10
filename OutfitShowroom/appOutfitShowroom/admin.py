from django.contrib import admin
from .models import Estilo, Ocasion, Outfit, Contacto
from django.utils.html import format_html
from django.templatetags.static import static

class EstiloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_en')
    search_fields = ('nombre', 'nombre_en')

class OcasionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_en')
    search_fields = ('nombre', 'nombre_en')

class OutfitAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'descripcion', 'precio', 'display_imagen')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('estilos', 'ocasion')

    def display_imagen(self, obj):
        if obj.imagen:
            # Generate the correct static file URL
            imagen_url = static(obj.imagen.url)
            
            # Adjust the width and height as needed
            return format_html('<img src="{}" width="50" height="50" />', imagen_url)
        else:
            return 'No Image'

admin.site.register(Estilo, EstiloAdmin)
admin.site.register(Ocasion, OcasionAdmin)
admin.site.register(Outfit, OutfitAdmin)
admin.site.register(Contacto)
