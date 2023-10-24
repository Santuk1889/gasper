from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Categoria, Movimiento
from .forms import CategoriaForm, MovimientoForm
from django.shortcuts import render, get_object_or_404

def renderizar_base(request):
    return render(request, 'app/base.html')

class CrearMovimientoView(CreateView):
    model = Movimiento
    form_class = MovimientoForm
    template_name = 'app/crear_movimiento.html'
    success_url = reverse_lazy('app:ver_movimientos')

    def form_valid(self, form):
        movimiento = form.save(commit=False)
        movimiento.categoria.total += movimiento.monto
        movimiento.categoria.save()
        movimiento.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

class VerMovimientosView(ListView):
    model = Movimiento
    template_name = 'app/ver_movimientos.html'
    context_object_name = 'movimientos'

    def get_queryset(self):
        fecha_inicio = self.request.GET.get('fecha_inicio')
        fecha_fin = self.request.GET.get('fecha_fin')
        categoria = self.request.GET.get('categoria')
        order_by = self.request.GET.get('order_by', '-fecha')
        queryset = Movimiento.objects.all()

        if fecha_inicio and fecha_fin:
            queryset = queryset.filter(fecha__range=(fecha_inicio, fecha_fin))

        if categoria:
            queryset = queryset.filter(categoria__id=categoria)

        return queryset.order_by(order_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        fecha_inicio = self.request.GET.get('fecha_inicio')
        fecha_fin = self.request.GET.get('fecha_fin')
        categoria = self.request.GET.get('categoria')
        mensaje_filtro = "Se han aplicado los siguientes filtros: "

        if fecha_inicio:
            mensaje_filtro += f"Fecha desde {fecha_inicio} "
        if fecha_fin:
            mensaje_filtro += f"hasta {fecha_fin} "
        if categoria:
            categoria_obj = Categoria.objects.get(id=categoria)
            mensaje_filtro += f"Categoría: {categoria_obj.nombre}"

        context['mensaje_filtro'] = mensaje_filtro
        context['order_by'] = self.request.GET.get('order_by', '-fecha')
        return context

class DetalleMovimientoView(DetailView):
    model = Movimiento
    template_name = 'app/detalle_movimiento.html'

class EditarMovimientoView(UpdateView):
    model = Movimiento
    form_class = MovimientoForm
    template_name = 'app/editar_movimiento.html'
    success_url = reverse_lazy('app:ver_movimientos')

    def form_valid(self, form):
        movimiento_anterior = get_object_or_404(Movimiento, pk=self.object.pk)
        monto_anterior = movimiento_anterior.monto
        response = super().form_valid(form)
        diferencia_monto = self.object.monto - monto_anterior
        movimiento_anterior.categoria.total -= diferencia_monto
        movimiento_anterior.categoria.save()
        self.object.categoria.total += self.object.monto
        self.object.categoria.save()
        return response

class EliminarMovimientoView(DeleteView):
    model = Movimiento
    template_name = 'app/eliminar_movimiento.html'
    success_url = reverse_lazy('app:ver_movimientos')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        monto_anterior = self.object.monto
        response = super().delete(request, *args, **kwargs)
        self.object.categoria.total -= monto_anterior
        self.object.categoria.save()
        return response

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

class EliminarCategoriaView(DeleteView):
    model = Categoria
    template_name = 'app/eliminar_categoria.html'
