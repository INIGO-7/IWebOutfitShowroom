from django.db import models 	

class Estilo(models.Model):
    def __str__(self):
        return self.nombre
    
    nombre = models.CharField(max_length=50)

class Ocasion(models.Model):
    def __str__(self):
        return self.nombre
    
    nombre = models.CharField(max_length=50)

class Outfit(models.Model):
    def __str__(self):
        return f'Nombre: {self.nombre}'
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=700)
    ocasion = models.ForeignKey(Ocasion, on_delete=models.CASCADE)
    estilos = models.ManyToManyField(Estilo)
    precio = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='static/img',blank=True,null=True,verbose_name='Image')
    fecha = models.DateTimeField(auto_now_add=True)
