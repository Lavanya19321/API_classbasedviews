from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.decorators import APIView
from rest_framework.response import Response

# Create your views here.
class productCurd(APIView):
    def get(self,request):
        POD=product.objects.all()
        JSOD=productmodelserializer(POD,many=True)
        return Response(JSOD.data)
    
    def post(self,request):
        JOD=request.data
        PDO=productmodelserializer(data=JOD)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'data inserted successfully'})
        else:
            return Response({'error':'data  is not inserted'})
    
