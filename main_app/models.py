from django.db import models

# Create your models here.

COLORS = (
    ('red', 'Red'),
    ('blu', 'Blue'),
    ('ylw', 'Yellow'),
    ('grn', 'Green'),
    ('brn', 'Brown')
    )

class Clothing(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=1, choices=COLORS, default=COLORS[0][0])

    def __str__(self):
        return self.name

class Color(models.Model):
    # color = models.ForeignKey(Clothing, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ComplimentaryColor(models.Model):
    # colors = 
    # def __str__(self):
    #     return self.name