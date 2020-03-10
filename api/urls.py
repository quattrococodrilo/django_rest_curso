from django.urls import path

from api.apiviews import ProductoDetalle, ProductoList

urlpatterns = [
    path(
        'v1/productos/',
        ProductoList.as_view(),
        name='producto_list'
    ),
    path(
        'v1/productos/<int:pk>',
        ProductoDetalle.as_view(),
        name='producto_detalle'
    ),
]
