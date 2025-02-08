from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet

# Create your views here.

from django.http import HttpResponse

def sayHello(request):
 return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

class bookingView(APIView):
    
    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookingSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "success",  "data" : serializer.data})
            
            
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticated]