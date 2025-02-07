from django.urls import path
from . import views

urlpatterns = [
    # path('', views.sayHello, name = 'sayHello'),
    path('', views.index, name='index'),
    # path('menu/', views.menu)
    path('booking/', views.bookingView.as_view(), name = 'booking'),
]
