from django.db import models

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

class Clothing(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE, default=TYPE[0][0])
    color = models.CharField(max_length=3, choices=COLORS, default=COLORS[0][0])

    def __str__(self):
        return self.name

# class Color(models.Model):
#     # color = models.ForeignKey(Clothing, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class ComplimentaryColor(models.Model):
#     # colors = 
#     # def __str__(self):
#     #     return self.name
