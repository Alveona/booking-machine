from django.shortcuts import render
from .serializers import RoomSerializer, BookingSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import Booking, Room

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    http_method_names = ['post', 'get']

class BookingView(APIView):
    def post(self, request):
        pass

    def get(self, request):
        pass
