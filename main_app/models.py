from django.db import models

# Create your models here.

class Clothing(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.ForeignKey(Clothing, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ComplimentaryColor(models.Model):
    colors = 
    # def __str__(self):
    #     return self.name