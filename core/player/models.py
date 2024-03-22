from django.db import models
from django.contrib.auth.models import User



class City(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=40)
    city = models.ForeignKey(City, on_delete=models.CASCADE , related_name='teams')

    def __str__(self):
        return self.name


class Coach(models.Model):
    full_name = models.CharField(max_length=40)
    city = models.ForeignKey(City, on_delete=models.CASCADE , related_name='coaches')
    team = models.ForeignKey(Team, on_delete=models.CASCADE , related_name='coach')

    def __str__(self):
        return self.full_name
    

class Player(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    born_date = models.DateTimeField()
    height = models.FloatField()
    weight = models.FloatField()
    team = models.ForeignKey(Team , on_delete=models.CASCADE , related_name='player')
    city = models.ForeignKey(City , on_delete=models.CASCADE , related_name='player')
    choices = [
        ('PG', 'Piont Guard'),
        ('SG', 'Shooting Guard'),
        ('SF', 'Small Forward'),
        ('PF', 'Power Forward'),
        ('C', 'Center'),
    ]
    position = models.CharField(max_length=20, unique=True, choices=choices)
    coach = models.ForeignKey(Coach , on_delete=models.CASCADE , related_name='player')

    def __str__(self):
        return f"{self.name} {self.surname} - {self.position} - {self.born_date}"
  