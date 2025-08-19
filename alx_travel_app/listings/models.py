from django.db import models

# Create your models here.
class Booking(models.Model):
  booking_id = models.PositiveIntegerField(primary_key=True, unique = True)
  start_date = models.DateTimeField(auto_now_add=True)
  end_date = models.DateTimeField(null= False)
  total_price = models.PositiveIntegerField(unique = True)
  class status(models.TextChoices):
    PENDING = 'pending', 'Pending'
    CONFIRMED = 'confirmed', 'Confirmed'
    ADMIN = 'admin', 'Admin'


class Review(models.Model):
  review_id = models.PositiveIntegerField(primary_key=True, auto_increment = True)
  rating = models.PositiveSmallIntegerField(null = False)
  comment = models.CharField(null = False)   

  

 
