from rest_framework import serializers
from api_app.models import User


class BuyerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'is_buyer','password','country','languages',)
        extra_kwargs = {"password":{"write_only":True}}


    def create(self, validated_data):
                
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        country = validated_data['country']
        languages = validated_data['languages']
        is_buyer = validated_data['is_buyer']
        user_obj = User(
            first_name = first_name,
            last_name = last_name,
            is_buyer = is_buyer,
            email = email,
            country = country,
            languages = languages
            )
        user_obj.set_password(validated_data['password'])
        user_obj.save()
        return user_obj


class SellerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'is_seller','password','country','languages','profile_image','skills','education','certification')
        extra_kwargs = {"password":{"write_only":True}}


    def create(self, validated_data):
        
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        country = validated_data['country']
        languages = validated_data['languages']
        is_seller = validated_data['is_seller']
        profile_image = validated_data['profile_image']
        skills = validated_data['skills'],
        education = validated_data['education'],
        certification = validated_data['certification']
        

        user_obj = User(
            first_name = first_name,
            last_name = last_name,
            is_seller = is_seller,            
            email = email,
            country = country,
            languages = languages,
            skills = skills,
            profile_image = profile_image,
            education = education,
            certification = certification
            )
        user_obj.set_password(validated_data['password'])
        user_obj.save()
        return user_obj

