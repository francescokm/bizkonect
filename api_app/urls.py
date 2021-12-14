
from django.urls import path, include, re_path
from api_app.views import SellerRegView, BuyerRegView, loginView, welcome


urlpatterns = [
    re_path(r'^', include('api_app.status.urls')),
    re_path(r'^', include('api_app.offers.urls')),
    re_path(r'^', include('api_app.category.urls')),
    re_path(r'^', include('api_app.subcategory.urls')),
    re_path(r'^', include('api_app.services.urls')),
    re_path(r'^', include('api_app.prices.urls')),
    path("seller/register/", SellerRegView.as_view(), name="seller_reg"),
    path("buyer/register/", BuyerRegView.as_view(), name="buyer_reg"),
    path("login/", loginView.as_view(), name="login"),
    path('api-auth/', include('rest_framework.urls')),
    path("", welcome.as_view(), name="welcome"),
]