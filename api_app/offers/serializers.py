from rest_framework import serializers
from api_app.offers.models import first_offer, second_offer
from api_app.notifications.models import Notification
from api_app.status.models import Status

class SecondOfferSerial(serializers.ModelSerializer):
    def create(self, validated_data):
        service_id = validated_data.get('service')
        buyer_id = validated_data.get('buyer')
        status_data = Status.objects.get(pk=2)

        data_for_notif = {
            "buyer" : buyer_id,
            "service" : service_id,
            "status" : status_data
        }

        notif = Notification.objects.create(**data_for_notif)
        notif.save()

        return second_offer.objects.create(**validated_data)

    class Meta :
        model = second_offer
        fields = '__all__' 
        read_only_fields = ('id',)

class FirstOfferSerial(serializers.ModelSerializer):
  
    def create(self, validated_data):        
        service_id = validated_data.get('service')
        buyer_id = validated_data.get('buyer')
        status_data = Status.objects.get(pk=1)
        data_for_notif = {
            "buyer" : buyer_id,
            "service" : service_id,
            "status" : status_data
        }

        notif = Notification.objects.create(**data_for_notif)
        notif.save()
        return first_offer.objects.create(**validated_data)


    class Meta :
        model = first_offer
        fields = ['id','service','default_price','offer_price','offer_start_date','offer_duration','buyer']
        read_only_fields = ('id',)


