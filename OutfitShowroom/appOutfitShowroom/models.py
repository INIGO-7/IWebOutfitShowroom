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
        estilos = ', '.join([e.nombre for e in self.estilo.all()])
        return f'Nombre: {self.nombre}, Ocasion: {self.ocasion}, Estilo: {estilos}, Precio: {self.precio}€'
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=700)
    ocasion = models.ForeignKey(Ocasion, on_delete=models.CASCADE)
    estilo = models.ManyToManyField(Estilo)
    precio = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')
    fecha = models.DateTimeField(auto_now_add=True)
