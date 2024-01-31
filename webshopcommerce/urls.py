from django.urls import path

from . import views

app_name = 'webshopcommerce'

urlpatterns = [
    path('', views.index,name='index'),
    path('productosPorCategoria/<int:categoria_id>',views.productosPorCategoria,name='productosPorCategorias'),
    path('productosPorNombre',views.productosPorNombre,name='productosPorNombre'),
    path('producto/<int:producto_id>',views.productoDetalle,name='producto')
]