from django.db import models
 
class Departamento(models.Model):
    def __str__(self):
        return self.nombre
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()

class Habilidad(models.Model):
    def __str__(self):
        return self.nombre
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
 
class Empleado(models.Model):
    def __str__(self):
        return self.nombre
    # Campo para la relación one-to-many (un empleado pertenece a un departamento)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # Campo para la relación many-to-many (un empleado tiene varias habilidades)
    habilidades = models.ManyToManyField(Habilidad)
    nombre = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    # Es posible indicar un valor por defecto mediante 'default'
    antiguedad = models.IntegerField(default=0)
    # Para permitir propiedades con valor null, añadiremos las opciones null=True, blank=True.       	