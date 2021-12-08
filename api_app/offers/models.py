from django.db import models
from api_app.services.models import Servs



#an offer from buyer to seller
class first_offer(models.Model):
    service = models.ForeignKey(Servs, related_name='first_offers', on_delete=models.CASCADE)
    default_price = models.DecimalField(max_digits=6, decimal_places=2)
    offer_price = models.DecimalField(max_digits=6, decimal_places=2)
    offer_start_date = models.DateTimeField()
    offer_duration = models.IntegerField()
    offer_status = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f'{self.id} ({self.service.title})'


#an offer from seller to buyer
class second_offer(models.Model):
    service = models.ForeignKey(Servs, related_name='second_offers', on_delete=models.CASCADE)
    first_offer = models.ForeignKey(first_offer, related_name='second_offer', on_delete=models.CASCADE)
    second_offer_price = models.DecimalField(max_digits=6, decimal_places=2)
    second_offer_start_date = models.DateTimeField()
    second_offer_duration = models.IntegerField()
    second_offer_status = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return f'{self.id} ({self.service.title})'