
from django.urls import path, include
from api_app.views import SellerRegView, BuyerRegView, loginView


urlpatterns = [
    path("seller/register/", SellerRegView.as_view(), name="seller_reg"),
    path("buyer/register/", BuyerRegView.as_view(), name="buyer_reg"),
    path("login/", loginView.as_view(), name="login"),
    path('api-auth/', include('rest_framework.urls')),
]