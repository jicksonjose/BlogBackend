from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from userapp.models import UserModel
import json
from userapp.serializer import *
# Create your views here.

@csrf_exempt

def viewall(request):
    if request.method == 'GET':
        userList = UserModel.objects.all()
        serililized_data =UserSerializer(userList,many=True)
        return HttpResponse(json.dumps(serililized_data.data))
    
    

@csrf_exempt
def add(request):
    if request.method == 'POST':
        receieved_data = json.loads(request.body)
        print(receieved_data)
        serialized_data  = UserSerializer(data=receieved_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return HttpResponse(json.dumps({"status": "added"}))    
        else:
            return HttpResponse(json.dumps({"status": "error"}))   