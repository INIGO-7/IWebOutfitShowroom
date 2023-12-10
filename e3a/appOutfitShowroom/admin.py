from django.contrib import admin
from .models import Estilo, Ocasion, Outfit, Contacto
from django.utils.html import format_html
from django.templatetags.static import static
from django.urls import reverse

from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group, Permission

class EstiloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_en', 'display_related_outfits')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related('outfit_set')
    
    def display_related_outfits(self, obj):
        outfits = obj.outfit_set.all()
        outfit_links = [
            format_html('<a href="{}" target="_blank">{}</a>', reverse('admin:appOutfitShowroom_outfit_change', args=[outfit.id]), outfit.get_nombre())
            for outfit in outfits
        ]
        return format_html(', '.join(outfit_links))
    
    display_related_outfits.short_description = 'Related Outfits'

class OcasionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_en', 'display_related_outfits')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related('outfit_set')
    
    def display_related_outfits(self, obj):
        outfits = obj.outfit_set.all()
        outfit_links = [
            format_html('<a href="{}" target="_blank">{}</a>', reverse('admin:appOutfitShowroom_outfit_change', args=[outfit.id]), outfit.get_nombre())
            for outfit in outfits
        ]
        return format_html(', '.join(outfit_links))
    
    display_related_outfits.short_description = 'Related Outfits'

class OutfitAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'precio', 'autor', 'descripcion', 'display_imagen')
    search_fields = ('nombre', 'descripcion', 'autor')
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
        

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nacimiento', 'email', 'telefono')
    search_fields = ('nombre', 'apellido', 'email', 'telefono')
        
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'grupos', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login')

    def grupos(self, obj):
        group_links = [
            format_html('<a href="{}" target="_blank">{}</a>', reverse('admin:auth_group_change', args=[group.id]), group.name)
            for group in obj.groups.all()
        ]
        return format_html(', '.join(group_links))
        
class CustomGroupAdmin(GroupAdmin):
    list_display = ('name', 'display_users', 'display_permissions')

    def display_users(self, obj):
        user_links = [
            format_html('<a href="{}" target="_blank">{}</a>', reverse('admin:auth_user_change', args=[user.id]), user.username)
            for user in obj.user_set.all()
        ]
        return format_html(', '.join(user_links))

    display_users.short_description = 'Miembros'


    def display_permissions(self, obj):
        permissions = obj.permissions.all()
        return ', '.join([permission.name for permission in permissions])

    display_permissions.short_description = 'Permissions'


admin.site.register(Estilo, EstiloAdmin)
admin.site.register(Ocasion, OcasionAdmin)
admin.site.register(Outfit, OutfitAdmin)
admin.site.register(Contacto, ContactoAdmin)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)