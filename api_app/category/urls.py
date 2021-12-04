
from django.urls import path
from api_app.category.views import CategoryView, DetailCategoryView, CategoryOnServicesView, CategoryOnServicesRetriveView


urlpatterns = [
    path("category/", CategoryView.as_view(), name="cat"),
    path("category/<int:pk>/", DetailCategoryView.as_view(), name="det_cat"),
    path("category/service/", CategoryOnServicesView.as_view(), name="cat_services"),    
    path("category/service/<int:pk>/", CategoryOnServicesRetriveView.as_view(), name="cat_retr_services"),    
]