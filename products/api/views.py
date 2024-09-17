from rest_framework import generics

from articles.models import Product
from .serializers import ArticleGETSerializer, ArticlePOSTSerializer

class ProductViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ArticleGETSerializer
