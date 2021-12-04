from django.urls import path
from api_app.subcategory.views import SubCategoryView,DetailSubCategoryView


urlpatterns = [
    path("subcategory/", SubCategoryView.as_view(), name="subcat"),
    path("subcategory/<int:pk>/", DetailSubCategoryView.as_view(), name="det_subcat"),
]