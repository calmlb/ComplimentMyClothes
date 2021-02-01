from django.db import models
from django.contrib.auth.models import User

# Create your models here.

COLORS = (
    ('red', 'Red'),
    ('blu', 'Blue'),
    ('ylw', 'Yellow'),
    ('grn', 'Green'),
    ('brn', 'Brown')
    )

TYPE = (
    ('tshirt', 'T-Shirt'),
    ('sweater', 'Sweater'),
    ('sweatshirt', 'Sweatshirt'),
    ('jacket', 'Jacket'),
    ('jeans', 'Jeans'),
    ('leggings', 'Leggings'), 
    ('shorts', 'Shorts')
    #  etc... 
    )

SEASON =(
    ('spring', 'Spring'),
    ('summer', 'Summer'),
    ('fall', 'Fall'),
    ('winter', 'Winter'),
    )

class Clothing(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE, default=TYPE[0][0])
    color = models.CharField(max_length=3, choices=COLORS, default=COLORS[0][0])
    season = models.CharField(max_length=10, choices=SEASON, default=SEASON[0][0])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.name

class Photo(models.Model):
    url = models.CharField(max_length=200)
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for clothing_id: {self.clothing_id} @{self.url}"