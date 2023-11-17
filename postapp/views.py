from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from postapp.models import PostModel
import json
from postapp.serializer import *
# Create your views here.

@csrf_exempt
def viewall(request):
    if request.method == 'GET':
        userList = PostModel.objects.all()
        serililized_data =PostSerializer(userList,many=True)
        return HttpResponse(json.dumps(serililized_data.data))
    
    

@csrf_exempt
def add(request):
    if request.method == 'POST':
        receieved_data = json.loads(request.body)
        print(receieved_data)
        serialized_data  = PostSerializer(data=receieved_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return HttpResponse(json.dumps({"status": "post added"}))    
        else:
            return HttpResponse(json.dumps({"status": "error"}))   