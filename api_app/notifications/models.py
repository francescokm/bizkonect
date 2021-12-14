from django.db import models
from api_app.models import User
from api_app.services.models import Servs
from api_app.status.models import Status

class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    service = models.ForeignKey(Servs, related_name='notifications', on_delete=models.CASCADE)
    status = models.ForeignKey(Servs, related_name='notifications', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    readed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['status.title']

    def __str__(self):
        return f'{self.id} ({self.status.title})'