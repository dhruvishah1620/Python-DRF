from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers import UserSerializer
from .models import User



# Create your views here.
@csrf_exempt
def addUser(request):
	data = JSONParser().parse( request )

	serializer = UserSerializer( data = data )
	if serializer.is_valid():
		serializer.save()
		return JsonResponse(serializer.data, status = status.HTTP_201_CREATED)
	return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def getAllUser(request):

	users = User.objects.all()

	serializer = UserSerializer( users, many=True )
	return JsonResponse( serializer.data, safe=False )

def getUser(request,pk):

	try:
		user = User.objects.get(pk=pk)
	except:
		return JsonResponse({"message":"Record not found"})
	
	serializer = UserSerializer(user)
	return JsonResponse(serializer.data)