from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.renderizar_base, name='renderizar_base'),
    path('movimientos/crear/', views.CrearMovimientoView.as_view(), name='crear_movimiento'),
    path('movimientos/', views.VerMovimientosView.as_view(), name='ver_movimientos'),
    path('movimientos/detalle/<int:pk>/', views.DetalleMovimientoView.as_view(), name='detalle_movimiento'),
    path('movimientos/editar/<int:pk>/', views.EditarMovimientoView.as_view(), name='editar_movimiento'),
    path('movimientos/eliminar/<int:pk>/', views.EliminarMovimientoView.as_view(), name='eliminar_movimiento'),  # Nueva URL para eliminar movimientos
    
    path('categorias/crear/', views.CrearCategoriaView.as_view(), name='crear_categoria'),
    path('categorias/', views.VerCategoriasView.as_view(), name='ver_categorias'),
    path('categorias/detalle/<int:pk>/', views.DetalleCategoriaView.as_view(), name='detalle_categoria'),
    path('categorias/editar/<int:pk>/', views.EditarCategoriaView.as_view(), name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', views.EliminarCategoriaView.as_view(), name='eliminar_categoria'),
    # Nueva URL para eliminar categorías
]
