from rest_framework import serializers
from .models import Room, Booking
from django.conf import settings
from django.contrib.auth import get_user_model
import time


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    room = serializers.SerializerMethodField()
    time_from = serializers.SerializerMethodField()
    time_until = serializers.SerializerMethodField()

    def get_room(self, obj):
        return obj.room.id

    def get_time_from(self, obj):
        return obj.time_from.strftime("%d.%m.%y %H:%M")

    def get_time_until(self, obj):
        return obj.time_until.strftime("%d.%m.%y %H:%M")

    class Meta:
        model = Booking
        fields = ('room', 'time_from', 'time_until')

User = settings.AUTH_USER_MODEL
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
