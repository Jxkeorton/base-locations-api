from django.db import models

class Location(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    rock_drop = models.IntegerField(null=True)
    total_height = models.IntegerField(null=True, blank=True)
    access = models.CharField(max_length=250)
    cliff_aspect = models.CharField(max_length=3)
    opened_by = models.CharField(max_length=100, null=True, blank=True)
    date_opened = models.DateField(null=True, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_qpihoy', blank=True, null=True
    )

    def __str__(self):
        return self.name

