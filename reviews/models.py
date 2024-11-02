from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey('locations.Location', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    hazard = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} by {self.owner.username} at {self.location.name}"
