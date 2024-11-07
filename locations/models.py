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
    access = models.CharField(max_length=250, null=True, blank=True)
    cliff_aspect = models.CharField(max_length=3, null=True, blank=True)
    opened_by = models.CharField(max_length=100, null=True, blank=True)
    date_opened = models.DateField(null=True, blank=True)
    image = models.URLField(
        default='https://res.cloudinary.com/dz02qubd3/image/upload/v1729441727/default_post_qpihoy.jpg', blank=True, null=True
    )

    def __str__(self):
        return self.name

