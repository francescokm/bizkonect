from django.urls import path
from api_app.offers.views import CreateFirstOfferView,DetailFirstOfferView
from api_app.offers.views import CreateSecondOfferView,DetailSecondOfferView

urlpatterns = [
    path("first_offer/", CreateFirstOfferView.as_view(), name="CreateFirstOfferView"),
    path("first_offer/<int:pk>/", DetailFirstOfferView.as_view(), name="DetailFirstOfferView"),
    path("second_offer/", CreateSecondOfferView.as_view(), name="CreateSecondOfferView"),
    path("second_offer/<int:pk>/", DetailSecondOfferView.as_view(), name="DetailSecondOfferView"),
]