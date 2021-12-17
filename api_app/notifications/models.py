from django.db import models
from api_app.services.models import Servs
from api_app.status.models import Status
from django.conf import settings

class Notification(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    service = models.ForeignKey(Servs, related_name='notifications', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, related_name='notifications', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    readed = models.BooleanField(default=False)
    

    def __str__(self):
        return f'{self.id} ({self.status.title})'