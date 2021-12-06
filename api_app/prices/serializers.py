from rest_framework import serializers
from api_app.prices.models import PriceServs

class PriceSerial(serializers.ModelSerializer):

    class Meta :
        model = PriceServs
        fields = '__all__' 
        read_only_fields = ('id',)
