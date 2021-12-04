from django.db import models
from api_app.category.models import Category

class SubCategory(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.id} ({self.name})'