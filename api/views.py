from __future__ import unicode_literals
 
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Items
# Create your views here.
 
class ItemsView(APIView):
    def get(self,request):
        if 'name' in request.GET:
            data  = Items.objects.filter(name=request.GET['name']).values('name','price').first()
        else:
            data  = Items.objects.all().values('name','price')
 
        return Response({"result":data},status=200)
 
    def post(self,request):
        data = request.data
        print(data)
        items_obj = Items.objects.create(name=data['name'], price=data['price'])
        return Response({"message":"created"}, status=202) 