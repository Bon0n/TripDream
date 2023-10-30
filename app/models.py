from django.contrib.auth.models import User
from django.db import models


class UserDetails(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    state_hometown = models.PositiveSmallIntegerField()
    hometown = models.PositiveSmallIntegerField()
    regenerate_map = models.BooleanField(default=True, null=True, blank=True)


class State(models.Model):
    state = models.CharField(max_length=40)
    uf = models.CharField(max_length=2)
    ibge_id = models.PositiveSmallIntegerField()
    country_id = models.PositiveSmallIntegerField()
    ddd = models.JSONField()


class City(models.Model):
    ibge_id = models.PositiveIntegerField()
    city = models.CharField(max_length=60)
    state_id = models.ForeignKey(
        State, on_delete=models.CASCADE
    )
    lat_lon = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    cod_tom = models.PositiveSmallIntegerField()


class VisitedCity(models.Model):
    city_id = models.ForeignKey(
        City, on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE
    )


class InterestedCity(models.Model):
    city_id = models.ForeignKey(
        City, on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE
    )


class PlanningCity(models.Model):
    city_id = models.ForeignKey(
        City, on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE
    )


class Photo(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    city_id = models.ForeignKey(
        City, on_delete=models.CASCADE
    )
    description = models.CharField(max_length=256)
    path = models.TextField()

