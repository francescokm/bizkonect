from rest_framework import generics
from api_app.notifications.models import Notification as M_Notif
from api_app.notifications.serializers import NotifSerial

class NotifView(generics.ListCreateAPIView):
    queryset = M_Notif.objects.all()
    serializer_class  = NotifSerial

class DetailNotifView(generics.RetrieveAPIView):
    queryset = M_Notif.objects.all()
    serializer_class  = NotifSerial