from rest_framework import serializers
from .models import Room, Booking
from django.conf import settings

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    room = serializers.SerializerMethodField()

    def get_room(self, obj):
        return obj.room.id

    class Meta:
        model = Booking
        fields = ('room', 'time_from', 'time_until')
