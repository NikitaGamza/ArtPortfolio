from django.contrib import admin
from .models import Category, Picture, Material

# Register your models here.
admin.site.register(Category)
admin.site.register(Picture)
admin.site.register(Material)