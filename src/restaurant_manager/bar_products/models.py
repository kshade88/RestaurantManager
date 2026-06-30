from django.db import models

# Create your models here.
class BarProduct(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Beer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Wine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Spirit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class liqueur(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bitters(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

