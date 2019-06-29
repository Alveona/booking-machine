from rest_framework import routers
from django.urls import path
from .views import BookingView, RoomViewSet, UserViewSet
# app_name = "api"


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'rooms', RoomViewSet, base_name='rooms')
router.register(r'register', UserViewSet, base_name='register')

urlpatterns = router.urls
urlpatterns += path('bookings', BookingView.as_view()),
