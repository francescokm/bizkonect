from rest_framework import generics
from api_app.status.models import M_Status
from api_app.status.serializers import StatusSerial

class StatusView(generics.ListCreateAPIView):
    queryset = M_Status.objects.all()
    serializer_class  = StatusSerial

class DetailStatusView(generics.RetrieveAPIView):
    queryset = M_Status.objects.all()
    serializer_class  = StatusSerial