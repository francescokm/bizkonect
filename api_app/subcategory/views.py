from rest_framework import generics
from rest_framework import generics
from api_app.subcategory.models import SubCategory as M_Sub
from api_app.subcategory.serializers import SubCategorySerial

class SubCategoryView(generics.ListCreateAPIView):
    queryset = M_Sub.objects.all()
    serializer_class  = SubCategorySerial

class DetailSubCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = M_Sub.objects.all()
    serializer_class  = SubCategorySerial