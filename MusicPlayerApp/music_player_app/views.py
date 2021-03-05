from django.shortcuts import render
from .models import SongModel
from .serializers import SongSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["GET"])
def Get_all_Song(request):
    songs=SongModel.object.all()
    song_list=SongSerializer(instance=songs,many=True)
    return Response(song_list.data)

@api_view(["GET"])
def Get_Song(request,pk):
    song=SongModel.object.get(id=pk)
    song_sr=SongSerializer(instance=song,many=False)
    return Response(song_sr.data)

@api_view(["POST"])
def Create_Song(request):
    song=SongSerializer(data=request.data)
    if song.is_valid():
        song.save()
    return Response("Song Has Been Created!")

@api_view(["DELETE"])
def Delete_Song(request,pk):
    song=SongModel.object.get(id=pk)
    song.delete()
    return Response("Your Song has been Deleted from Music Player!")

@api_view(["PUT"])
def Update_Song(request,pk):
    song=SongModel.object.get(id=pk)
    song_sr=SongSerializer(instance=song,id=pk)
    if song_sr.is_valid():
        song_sr.save()
    return Response(song_sr.data)
