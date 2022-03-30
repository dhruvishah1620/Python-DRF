from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

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
	return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def getAllUser(request):

	users = User.objects.all()

	serializer = UserSerializer( users, many=True )
	return JsonResponse( serializer.data, safe=False )

def getUser(request,pk):

	try:
		user = User.objects.get(pk=pk)
	except:
		return JsonResponse({"message":"Record not found"})
	
	if request.method == 'GET':
		serializer = UserSerializer(user)
		return JsonResponse(serializer.data)

@csrf_exempt
def update_user(request,pk):

	try:
		user = User.objects.get(pk=pk)
	except:
		return JsonResponse({"message":"Record not found"})

	userData = JSONParser().parse(request)
	s1 = UserSerializer(user,data=userData)
	if s1.is_valid():
		s1.save()
		return JsonResponse(s1.data, status = status.HTTP_201_CREATED)
	return JsonResponse(s1.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def deleteUser(request,pk):

	try:
		user = User.objects.get(pk=pk)
	except:
		return JsonResponse({"message":"Record not found"})
	user.delete()
	return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
