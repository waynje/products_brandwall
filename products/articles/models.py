from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(
        'Название',
        blank=False,
        max_length=128
    )
    description = models.TextField(
        'Описание',
        blank=False
    )
    price = models.DecimalField(
        'Цена',
        validators=[MinValueValidator(1)],
        max_digits=8,
        decimal_places=2
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self) -> str:
        return self.name
