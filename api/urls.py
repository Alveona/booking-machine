from rest_framework import routers
from django.urls import path
from .views import BookingView, RoomViewSet
app_name = "api"


router = routers.DefaultRouter(trailing_slash=True)
router.register(r'rooms', RoomViewSet, base_name='rooms')

urlpatterns = router.urls
urlpatterns += path('bookings', BookingView.as_view()),
