from rest_framework import serializers
from api_app.category.models import Category as M_Category
from api_app.subcategory.models import SubCategory as M_SubCategory

class SubCategorySerial(serializers.ModelSerializer):

    class Meta :
        model = M_SubCategory
        fields = ['id','name','category']
        read_only_fields = ('id',)

class SubCategoryRelatedSerial(serializers.ModelSerializer):

    class Meta :
        model = M_SubCategory
        fields = ['id','name']
        read_only_fields = ('id',)

