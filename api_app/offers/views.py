from rest_framework import generics
from api_app.offers.models import first_offer as M_1, second_offer as M_2
from api_app.offers.serializers import FirstOfferSerial,SecondOfferSerial

class CreateFirstOfferView(generics.CreateAPIView):
    queryset = M_1.objects.all()
    serializer_class  = FirstOfferSerial

class DetailFirstOfferView(generics.UpdateAPIView):
    queryset = M_1.objects.all()
    serializer_class  = FirstOfferSerial


class CreateSecondOfferView(generics.CreateAPIView):
    queryset = M_2.objects.all()
    serializer_class  = SecondOfferSerial

class DetailSecondOfferView(generics.UpdateAPIView):
    queryset = M_2.objects.all()
    serializer_class  = SecondOfferSerial