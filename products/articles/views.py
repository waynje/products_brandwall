from typing import Any

from django.db.models.query import QuerySet
from django.views.generic import ListView
from rest_framework.views import APIView

from articles.models import Product

class GetProducts(ListView):
    data = Product.objects.all()
    template_name = 'articles/get.html'
    context_object_name = 'data'

    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.all()


class PostProducts(APIView):

    def post(self, request):
        name = request.data.get('name')
        description = request.data.get('description')
        price = request.data.get('price')
