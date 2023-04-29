from django.db import models

# Create your models here.
class Listings(models.Model):
    # we can skip defining primary_key id - Django will do itself.
    name = models.TextField(max_length=1500)
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    longitude = models.TextField(max_length=1500)
    latitude = models.TextField(max_length=1500)
    city = models.TextField(max_length=1500)
    neighbourhood = models.TextField(max_length=1500)
    listing_id = models.ForeignKey(Listings, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Reviews(models.Model):
    score_rating = models.PositiveIntegerField()
    score_value = models.PositiveIntegerField()
    listing_id = models.ForeignKey(Listings, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Property_Details(models.Model):
    property_type = models.TextField(max_length=1500)
    room_type = models.TextField(max_length=1500)
    accomodate_count = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    instant_bookable = models.CharField(max_length=150)
    listing_id = models.ForeignKey(Listings, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Amenities(models.Model):
    amenities = models.TextField(max_length=10000)
    listing_id = models.ForeignKey(Listings, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name