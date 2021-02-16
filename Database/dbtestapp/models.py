from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Criclet(models.Model):
    Player_name = models.CharField(max_length=30)
    Player_role = models.CharField(max_length=30)
    Player_position = models.CharField(max_length=30)    