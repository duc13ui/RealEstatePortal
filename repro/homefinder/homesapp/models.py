from django.db import models

# Create your models here.

# Location Model which will inherit from models.Model
class Location(models.Model):
    location_name = models.CharField(max_length = 200) # Name of location
    location_type = models.CharField(max_length = 200) # Type of location

    def __str__(self):
        return self.location_name

class Property(models.Model):
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    property_name = models.CharField(max_length = 200)
    area = models.CharField(max_length = 200)

    age = models.CharField(max_length = 200)
    price = models.CharField(max_length = 200)
    direction = models.CharField(max_length = 200)
    floor = models.CharField(max_length = 200)
    postadd = models.CharField(max_length = 200)
    image_url = models.CharField(max_length = 500)
    lat_field = models.CharField(max_length = 200)
    long_field = models.CharField(max_length = 200)

    def __str__(self):
        return self.property_name

