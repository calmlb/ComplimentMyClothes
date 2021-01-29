from django.db import models

# Create your models here.

class Clothing(models.Model):

    def __str__(self):
        return self.name

class Color(models.Model):
    color = models.ForeignKey(Clothing, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ComplimentaryColor(models.Model):
    
    def __str__(self):
        return self.name