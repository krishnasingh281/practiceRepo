from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializer(serializers.Serializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
class BookingSerializer(serializers.Serializer):
    class Meta:
        model =Booking
        fields ='__all__'