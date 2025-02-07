from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer

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
            