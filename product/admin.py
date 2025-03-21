
from django.contrib import admin


from .models import Plant, Category, Tag, PlantImage




@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class PlantAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class PlantAdmin(admin.ModelAdmin):
    pass

@admin.register(PlantImage)
class PlantAdmin(admin.ModelAdmin):
    pass