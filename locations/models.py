from django.db import models

class Location(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    coordinates = models.FloatField()
    rock_drop = models.IntegerField()
    total_height = models.IntegerField()
    access = models.CharField(max_length=250)
    cliff_aspect = models.CharField(max_length=3)
    opened_by = models.CharField(max_length=100, null=True, blank=True)
    date_opened = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

