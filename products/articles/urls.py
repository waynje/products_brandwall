from django.urls import include, path

from .views import GetProducts, PostProducts

urlpatterns = [
    path('get/', GetProducts.as_view(), name='get_products'),
    path('post_product/', PostProducts.as_view(), name='post_product')
]
