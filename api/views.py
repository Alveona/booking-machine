from django.shortcuts import render
from django.conf import settings
from .serializers import RoomSerializer, BookingSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import Booking, Room
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
import dateutil.parser

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post', 'get']

class BookingView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        room = request.data.get('room')
        try:
            room_object = Room.objects.all().get(id = room)
        except:
            return Response({"response":"no such room"}, status=status.HTTP_400_BAD_REQUEST)
        time_from = request.data.get('time_from')
        parsed_from = dateutil.parser.parse(time_from)
        time_until = request.data.get('time_until')
        parsed_until = dateutil.parser.parse(time_until)
        user = request.user
        booking = Booking(time_from = parsed_from, time_until = parsed_until, room = room_object, user = user)
        booking.save()
        return Response({"room":room,"time_from":time_from, "time_until":time_until}, status = status.HTTP_201_CREATED)
    def get(self, request):
        time_from = self.request.query_params.get('time_from')
        time_until = self.request.query_params.get('time_until')
        parsed_from = dateutil.parser.parse(time_from)
        parsed_until = dateutil.parser.parse(time_until)
        room = self.request.query_params.get('room')
        try:
            room_object = Room.objects.all().get(id = room)
        except:
            return Response({"response":"no such room"}, status=status.HTTP_400_BAD_REQUEST)
        bookings = Booking.objects.all().filter(time_from__gte = parsed_from, time_until__lte = parsed_until, room = room_object)
        return Response(BookingSerializer(bookings, many=True).data, status = status.HTTP_200_OK)
# User = settings.AUTH_USER_MODEL
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post']
