from django.urls import path
from api_app.services.views import ServiceView, DetailServView

urlpatterns = [
    path("service/", ServiceView.as_view(), name="serv"),
    path("service/<int:pk>/", DetailServView.as_view(), name="det_serv"),
]