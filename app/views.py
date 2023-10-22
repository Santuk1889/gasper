from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Categoria, Movimiento
from .forms import CategoriaForm, MovimientoForm
from django.shortcuts import render

def renderizar_base(request):
    return render(request, 'app/base.html')

class CrearMovimientoView(CreateView):
    model = Movimiento
    form_class = MovimientoForm
    template_name = 'app/crear_movimiento.html'
    success_url = reverse_lazy('app:ver_movimientos')

class VerMovimientosView(ListView):
    model = Movimiento
    template_name = 'app/ver_movimientos.html'

class DetalleMovimientoView(DetailView):
    model = Movimiento
    template_name = 'app/detalle_movimiento.html'

class EditarMovimientoView(UpdateView):
    model = Movimiento
    form_class = MovimientoForm
    template_name = 'app/editar_movimiento.html'
    success_url = reverse_lazy('app:ver_movimientos')

class CrearCategoriaView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'app/crear_categoria.html'
    success_url = reverse_lazy('app:ver_categorias')

class VerCategoriasView(ListView):
    model = Categoria
    template_name = 'app/ver_categorias.html'

class DetalleCategoriaView(DetailView):
    model = Categoria
    template_name = 'app/detalle_categoria.html'

class EditarCategoriaView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'app/editar_categoria.html'
    success_url = reverse_lazy('app:ver_categorias')
