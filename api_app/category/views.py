from rest_framework import generics
from rest_framework import generics
from api_app.category.models import Category as M_Cat
from api_app.category.serializers import CategorySerial

class CategoryView(generics.ListCreateAPIView):
    queryset = M_Cat.objects.all()
    serializer_class  = CategorySerial

class DetailCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = M_Cat.objects.all()
    serializer_class  = CategorySerial
