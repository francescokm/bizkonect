from django.db import models
from api_app.category.models import Category
from api_app.subcategory.models import SubCategory
from api_app.prices.models import PriceServs
from api_app.models import User

def get_service_image_filepath(self, filename):
    return f'service_image/{str(self.pk)}/{"service_image.png"}'

def get_default_service_image():
    return 'bizkonect/logo_1080_1080.png'
    
class Servs(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, unique=True)
    prices = models.ForeignKey(PriceServs, related_name='prices', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='services', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name='subcategories', on_delete=models.CASCADE)
    service_image = models.ImageField(null=True, upload_to=get_service_image_filepath,blank=True,default=get_default_service_image)
    tags = models.TextField(blank=True, null=True)
    pricing = models.DecimalField(max_digits=6, decimal_places=2)
    revision = models.IntegerField()
    delivery = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['title','created','updated',]

    def __str__(self):
        return f'{self.id} ({self.title})'