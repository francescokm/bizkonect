from rest_framework import serializers
from api_app.services.models import Servs as M_Services


class ServiceSerial(serializers.ModelSerializer):
    

    class Meta :
        model = M_Services
        fields = ['id','title', 'category','subcategory','service_image','tags','pricing','revision','delivery','description','user']
        read_only_fields = ('id',)