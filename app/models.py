# app/models.py
from django.db import models

class Categoria(models.Model):
    INGRESO = "I"
    EGRESO = "E"
    TIPO_CHOICES = [
        (INGRESO, "Ingreso"),
        (EGRESO, "Egreso"),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    categoria_padre = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE
    )
    nivel_importancia = models.IntegerField(default=1)

    def __str__(self):
        return self.nombre

class Movimiento(models.Model):
    fecha = models.DateField()
    concepto = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.concepto} - {self.fecha}"
