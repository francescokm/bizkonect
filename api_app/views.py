from django.shortcuts import render
from .models import User
from .serializers import SellerSerializer, BuyerSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views import View
import datetime


class SellerRegView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SellerSerializer

class BuyerRegView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = BuyerSerializer


class loginView(APIView):

    def post(self, request, format=None):
        email = request.data['email']       
        password = request.data['password'] 
        user = authenticate(email=email, password=password)
        # user = User.objects.get(email=email)
        print(user)
        if user is not None:
            return Response({"Message": 
            {
                "user id":user.id,
                "message":"User Exist"
            
            }}, status=status.HTTP_200_OK)
        else:
            return Response({"Message": "User Does Not exist!"}, status=status.HTTP_404_NOT_FOUND)

        

class welcome(View):
    def get(self, request):        
        now = datetime.datetime.now()
        html = "<html><body><h1>Welcome</h1><h2>It is now %s.</h2></body></html>" % now
        return HttpResponse(html)