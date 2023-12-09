from django.contrib import admin
from .models import Estilo, Ocasion, Outfit

class OutfitAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'descripcion', 'precio', 'imagen')
    search_fields = ('nombre',)
    list_filter = ('estilos', 'ocasion')

admin.site.register(Estilo)
admin.site.register(Ocasion)
admin.site.register(Outfit, OutfitAdmin)