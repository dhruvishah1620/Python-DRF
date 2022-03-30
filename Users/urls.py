from django.urls import path
from . import views

urlpatterns = [
    path('addUser/', views.addUser, name="addUser"),
    path('allUser/', views.getAllUser, name="allUser"),
    path('user/<int:pk>', views.getUser, name="getUser"),
    path('updateUser/<int:pk>', views.update_user, name="updateUser"),
    path('deleteUser/<int:pk>', views.deleteUser, name="deleteUser"),
]