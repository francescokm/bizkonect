from rest_framework import serializers
from api_app.offers.models import first_offer
from api_app.services.models import Servs as M_Services
from api_app.prices.serializers import PriceSerial
from api_app.offers.serializers import FirstOfferSerial,SecondOfferSerial

class ServiceSerial(serializers.ModelSerializer):
    prices = PriceSerial(many=True, read_only=True)
    first_offers = FirstOfferSerial(many=True, read_only=True)
    second_offers = SecondOfferSerial(many=True, read_only=True)

    class Meta :
        model = M_Services
        fields = ['id','title', 'category','subcategory','service_image','tags','pricing','revision','delivery','description','prices','first_offers','second_offers','user']
        read_only_fields = ('id',)