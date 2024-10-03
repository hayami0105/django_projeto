from django.contrib import admin
from .models import Category, Recipe

#Uma forma
class CategoryAdmin(admin.ModelAdmin):
    ...
admin.site.register(Category, CategoryAdmin)

#Outra forma mesmo efeito
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...