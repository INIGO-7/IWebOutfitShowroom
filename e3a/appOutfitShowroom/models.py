from django.db import models 
from django.utils.translation import get_language	

class Estilo(models.Model):
    def __str__(self):
        return self.nombre
    
    def get_nombre(self):
        return self.nombre_en if get_language() == 'en' else self.nombre
    
    nombre = models.CharField(max_length=50)
    nombre_en = models.CharField(max_length=50, blank=True)

class Ocasion(models.Model):
    def __str__(self):
        return self.nombre
    
    def get_nombre(self):
        return self.nombre_en if get_language() == 'en' else self.nombre
    
    nombre = models.CharField(max_length=50)
    nombre_en = models.CharField(max_length=50, blank=True)

class Outfit(models.Model):

    def __str__(self):
        return f'Nombre: {self.nombre}'
    
    def get_nombre(self):
        return self.nombre_en if get_language() == 'en' else self.nombre
    
    def get_descripcion(self):
        return self.descripcion_en if get_language() == 'en' else self.descripcion
    
    def get_precio(self):
        return round((self.precio * 1.08),2) if get_language() == 'en' else self.precio
    
    nombre = models.CharField(max_length=200)
    nombre_en = models.CharField(max_length=200, blank=True)
    descripcion = models.TextField(max_length=700)
    descripcion_en = models.TextField(max_length=700, blank=True)
    ocasion = models.ForeignKey(Ocasion, on_delete=models.CASCADE)
    estilos = models.ManyToManyField(Estilo)
    precio = models.IntegerField(default=0)
    autor = models.CharField(max_length=25, blank=True)
    imagen = models.ImageField(upload_to='static/img',blank=True,null=True,verbose_name='Image')
    fecha = models.DateTimeField(auto_now_add=True)

class Contacto(models.Model):

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.telefono}'

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    email = models.CharField(max_length=50)
    telefono = models.IntegerField()