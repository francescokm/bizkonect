from rest_framework import serializers
from api_app.offers.models import first_offer, second_offer

class SecondOfferSerial(serializers.ModelSerializer):
    
    class Meta :
        model = second_offer
        fields = '__all__' 
        read_only_fields = ('id',)

class FirstOfferSerial(serializers.ModelSerializer):
    second_offer = SecondOfferSerial(many=True, read_only=True)

    class Meta :
        model = first_offer
        fields = ['id','service','default_price','offer_price','offer_start_date','offer_duration','offer_status','second_offer']
        read_only_fields = ('id',)


