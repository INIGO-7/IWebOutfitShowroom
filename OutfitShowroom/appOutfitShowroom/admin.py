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
    list_display = ('nombre', 'fecha', 'precio', 'autor', 'descripcion', 'display_imagen')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('estilos', 'ocasion')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user_groups = [group.name for group in request.user.groups.all()]

        # Check if the user is in the Influencer group
        if 'Influencer' in user_groups:
            # Filter queryset to show only outfits uploaded by the user
            return qs.filter(autor=request.user.username)
        else:
            return qs

    def display_imagen(self, obj):
        if obj.imagen:
            imagen_url = static(obj.imagen.url)
            return format_html('<img src="{}" width="50" height="50" />', imagen_url)
        else:
            return 'No Image'
        
class MyAdminSite(admin.AdminSite):
    site_header = 'My Custom Admin'
    site_title = 'My Admin Site'

admin_site = MyAdminSite(name='myadmin')


admin.site.register(Estilo, EstiloAdmin)
admin.site.register(Ocasion, OcasionAdmin)
admin.site.register(Outfit, OutfitAdmin)
admin.site.register(Contacto)
