from rest_framework import generics
from rest_framework import generics
from api_app.prices.models import PriceServs
from api_app.prices.serializers import PriceSerial

class PriceServiceView(generics.ListCreateAPIView):
    queryset = PriceServs.objects.all()
    serializer_class  = PriceSerial

class DetailPriceServView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriceServs.objects.all()
    serializer_class  = PriceSerial