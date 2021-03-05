from django.urls import path
from . import views

urlpatterns = [
    path('Audio/',views.Get_all_Song,name="Get_all_Song"),
    path('Audio/<str:pk>/',views.Get_Song,name="Get_Song"),
    path('Update/Audio/<str:pk>/',views.Update_Song,name="Update_Song"),
    path('Create/Audio/',views.Create_Song,name="Create_Song"),
    path('Delete/Audio/<str:pk>/',views.Delete_Song,name="Delete_Song"),

]