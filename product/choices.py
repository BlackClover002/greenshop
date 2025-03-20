from django.db import models

class PlantSizeChoices(models.TextChoices):
    SMALL = 'SMALL', 'Small'
    LARGE = 'LARGE', 'Large'
    MEDIUM = 'MEDIUM', 'Medium'