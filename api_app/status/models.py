from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    message = models.TextField()
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.id} ({self.name})'