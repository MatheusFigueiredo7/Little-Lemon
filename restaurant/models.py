from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self) -> str:
        return self.title
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.name