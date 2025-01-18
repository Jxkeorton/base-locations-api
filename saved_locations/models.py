from django.db import models
from django.contrib.auth.models import User


class SavedLocation(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='saved_locations'
    )
    location = models.ForeignKey(
        'locations.Location', on_delete=models.CASCADE, related_name='saved_by'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'location']  # Prevents duplicate saves
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner.username} saved {self.location.name}"
