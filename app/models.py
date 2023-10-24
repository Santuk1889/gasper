from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

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
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nombre

    def actualizar_total(self):
        # Calcular el total sumando los montos de los movimientos relacionados
        if self.pk is not None:
            total = Movimiento.objects.filter(categoria=self).aggregate(total=models.Sum('monto'))['total'] or 0.00
            self.total = total
            self.save()

    def save(self, *args, **kwargs):
        # Antes de guardar, actualiza el total
        self.actualizar_total()
        super(Categoria, self).save(*args, **kwargs)

class Movimiento(models.Model):
    fecha = models.DateField()
    concepto = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.concepto} - {self.fecha}"

@receiver(post_save, sender=Movimiento)
@receiver(post_delete, sender=Movimiento)
def actualizar_categoria_total(sender, instance, **kwargs):
    # Esto actualiza la categoría relacionada cuando se guarda o elimina un movimiento
    instance.categoria.actualizar_total()

