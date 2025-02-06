from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.PositiveIntegerField()
    Booking_date = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return self.name
    
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.IntegerField()
    
    def __str__(self):
        return self.title
    
    