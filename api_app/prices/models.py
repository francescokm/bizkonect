from django.db import models

class PriceServs(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    subtitle = models.CharField(max_length=50, blank=False, null=False)
    pricing = models.DecimalField(max_digits=6, decimal_places=2)
    benefits = models.TextField(blank=False, null=False)
    non_benefits = models.TextField(blank=True, null=True)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['title','created','updated',]

    def __str__(self):
        return f'{self.id} ({self.title})'