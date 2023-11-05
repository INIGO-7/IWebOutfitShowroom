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
        return f'Nombre: {self.nombre}, Ocasion: {self.ocasion}, Estilo: {self.estilo}, Precio: {self.precio}€'
    
    nombre = models.CharField(max_length=200)
    ocasion = models.ManyToManyField(Ocasion)
    estilo = models.ManyToManyField(Estilo)
    precio = models.IntegerField(default=0)
