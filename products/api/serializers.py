from rest_framework.serializers import ModelSerializer, ValidationError

from articles.models import Product


class ArticleGETSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ArticlePOSTSerializer(ArticleGETSerializer):

    def validate_name(self, name):
        if len(name.strip()) == 0:
            raise ValidationError('Название продукта не может быть пустым.')
        return name

    def validate_price(self, price):
        if price <= 0:
            raise ValidationError('Цена может быть только положительной.')
        return price
