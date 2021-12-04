from rest_framework import serializers
from api_app.category.models import Category as M_Category
from api_app.subcategory.serializers import SubCategoryRelatedSerial


class CategorySerial(serializers.ModelSerializer):
    subcategories = SubCategoryRelatedSerial(many=True, read_only=True)

    class Meta :
        model = M_Category
        fields = ['id','name', 'subcategories']
        read_only_fields = ('id',)