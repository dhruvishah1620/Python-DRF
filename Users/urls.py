from django.urls import path
from . import views

urlpatterns = [
    path('addUser/', views.addUser, name="addUser"),
    path('allUser/', views.getAllUser, name="allUser"),
    path('user/<int:pk>', views.getUser, name="getUser"),
]