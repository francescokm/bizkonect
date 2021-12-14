from rest_framework import serializers
from api_app.notifications.models import Notification

class NotifSerial(serializers.ModelSerializer):
    
    class Meta :
        model = Notification
        fields = '__all__' 
        read_only_fields = ('id',)



