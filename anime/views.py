from django.shortcuts import render
from rest_framework import generics
from .serializer import AnimeSerializer
from .models import Anime
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

class AnimeList(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Anime.objects.all()
  serializer_class = AnimeSerializer

class AnimeDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Anime.objects.all()
  serializer_class = AnimeSerializer
