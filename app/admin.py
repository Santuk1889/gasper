from django.contrib import admin
from .models import Categoria, Movimiento

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'nivel_importancia')
    list_filter = ('tipo', 'nivel_importancia')
    search_fields = ('nombre',)

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'concepto', 'monto', 'categoria')
    list_filter = ('fecha', 'categoria')
    search_fields = ('concepto',)
