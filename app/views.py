from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.decorators import APIView
from rest_framework.response import Response

# Create your views here.
class productCurd(APIView):
    def get(self,request,id):
        POD=product.objects.all()#orm
        #POD=product.objects.get(id=id)
        JSOD=productmodelserializer(POD,many=True)#json
        return Response(JSOD.data)
    
    def post(self,request,id):
        JOD=request.data
        PDO=productmodelserializer(data=JOD)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'data inserted successfully'})
        else:
            return Response({'error':'data  is not inserted'})
        
    def put(self,request,id):
        PO=product.objects.get(id=id)
        UPDO=productmodelserializer(PO,data=request.data)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'data is updated successfully'})
        else:
            return Response({'error':'data  is not inserted'})
        
    def patch(self,request,id):
        PO=product.objects.get(id=id)
        UPDO=productmodelserializer(PO,data=request.data,partial=True)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'data is updated successfully'})
        else:
            return Response({'error':'data  is not inserted'})
        

    def delete(self,request,id):
        product.objects.get(id=id).delete()
        return Response({'delete':'data deleted successfully'})
    
