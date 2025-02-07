from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):  # ✅ Use ModelSerializer
    class Meta:
        model = Menu
        fields = '__all__'  # ✅ Corrected syntax

class BookingSerializer(serializers.ModelSerializer):  # ✅ Use ModelSerializer
    class Meta:
        model = Booking
        fields = '__all__'  # ✅ Corrected syntax
