
from django.db import models
from product.choises import PlantSizeChoices
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os


class Category(models.Model):
    sku = models.CharField(
        max_length=15,
        unique=True,
        verbose_name='Серийный номер',
    )
    Category = models.ManyToManyField(
        to='product.Category',
        related_name='plants',
        verbose_name='Категория',
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Категория",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"  #

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Тег",
    )

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Тeги"

    def __str__(self):
        return self.name


class Plant(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название",
    )
    short_description = models.CharField(
        max_length=255,
        verbose_name="Краткое описание",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Цена"
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0.00,
        verbose_name="Рейтинг"
    )
    size = models.CharField(
        max_length=50,
        choices=PlantSizeChoices,
        default=PlantSizeChoices.MEDIUM,
    )
    tags = models.ManyToManyField(
        to=Tag,
        related_name='plants',
        verbose_name='Теги',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "Растения"
        verbose_name_plural = "Растении"
        ordering = ['-updated_at']


class PlantImage(models.Model):
    plant = models.ForeignKey(
        to=Plant,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Изображение',
    )
    image = models.ImageField(
        upload_to='images/plants/',
        verbose_name='Изображение',
    )

    class Meta:
        verbose_name = "Изображение растения"
        verbose_name_plural = "Изображении растений"


class Cart(models.Model):
    plant = models.ForeignKey(
        to=Plant,
        related_name='carts',
        on_delete=models.CASCADE,
        verbose_name='Корзина',
    )
    added_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
        ordering = ['-added_at']

    def __str__(self):
        return self.plant.name


@receiver(post_delete, sender=Plant)
def plant_delete_receiver(sender, instance, **kwargs):
    if hasattr(instance, 'images'):
        for image in instance.images.all():
            if os.path.exists(image.image.path):
                os.remove(image.image.path)
            image.delete()
