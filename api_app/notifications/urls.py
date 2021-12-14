from django.urls import path
from api_app.notifications.views import NotifView, DetailNotifView

urlpatterns = [
    path("notif/", NotifView.as_view(), name="notif"),
    path("notif/<int:pk>/", DetailNotifView.as_view(), name="notifdetail"),
]