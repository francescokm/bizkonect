from django.urls import path
from api_app.status.views import StatusView, DetailStatusView

urlpatterns = [
    path("status/", StatusView.as_view(), name="status"),
    path("status/<int:pk>/", DetailStatusView.as_view(), name="det_status"),
]