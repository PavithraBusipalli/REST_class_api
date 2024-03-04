from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import APIView
from rest_framework.response import Response


# Create your views here.

class ProductCategoryJsonData(APIView):
    def get(self,request):
        PMO = ProductCategory.objects.all()
        JSS = ProductCatSerializer(PMO,many=True)
        JSD = JSS.data
        return Response(JSD)
    def post(self,request):
        MDO = request.data
        PDO = ProductCatSerializer(data=MDO)
        if PDO.is_valid():
            PDO.save()
            return Response('Inserted Successfully')
        else:
            return Response('Invalid Data Under Process')
        
class ProductJsonData(APIView):
    def get(self,request):
        PMO = Product.objects.all()
        JSS = ProductSerializer(PMO,many = True)
        JSD = JSS.data
        return Response(JSD)
    def post(self,request):
        MDO = request.data
        PDO = ProductSerializer(data = MDO)
        if PDO.is_valid():
            PDO.save()
            return Response('Product Inserted Successfully')
        else:
            return Response('Invalid ')

    
        
        
    

