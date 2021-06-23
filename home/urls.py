from django.urls import path
from .views import home_view, list_products, edit_products

urlpatterns = [
    path('', home_view),
    path('listar_produtos/', list_products, name='list_products'),
    path('editar_produtos/<product_id>', edit_products, name='edit_products')
]