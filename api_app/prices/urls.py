from django.urls import path
from api_app.prices.views import PriceServiceView, DetailPriceServView

urlpatterns = [
    path("price/", PriceServiceView.as_view(), name="priceserv"),
    path("price/<int:pk>/", DetailPriceServView.as_view(), name="det_priceserv"),
]