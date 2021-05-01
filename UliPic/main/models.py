from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Material(models.Model):
    materia = models.CharField(max_length=250)

    def __str__(self):
        return self.materia

class Picture(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(blank=True, max_length=250)
    width = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    year = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    material = models.ManyToManyField(Material)

    def __str__(self):
        return self.name
