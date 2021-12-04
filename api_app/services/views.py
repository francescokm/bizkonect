from rest_framework import generics
from rest_framework import generics
from api_app.services.models import Servs as M_Serv
from api_app.services.serializers import ServiceSerial

class ServiceView(generics.ListCreateAPIView):
    queryset = M_Serv.objects.all()
    serializer_class  = ServiceSerial

class DetailServView(generics.RetrieveUpdateDestroyAPIView):
    queryset = M_Serv.objects.all()
    serializer_class  = ServiceSerial