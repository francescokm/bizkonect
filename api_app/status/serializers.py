from rest_framework import serializers
from api_app.status.models import Status

class StatusSerial(serializers.ModelSerializer):
    
    class Meta :
        model = Status
        fields = '__all__' 
        read_only_fields = ('id',)



