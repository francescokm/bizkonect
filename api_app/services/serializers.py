from rest_framework import serializers
from api_app.services.models import Servs as M_Services
from api_app.prices.serializers import PriceSerial

class ServiceSerial(serializers.ModelSerializer):
    prices = PriceSerial(many=True, read_only=True)

    class Meta :
        model = M_Services
        fields = ['id','title', 'category','subcategory','service_image','tags','pricing','revision','delivery','description','prices']
        read_only_fields = ('id',)