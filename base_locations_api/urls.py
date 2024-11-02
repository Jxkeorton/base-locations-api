from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('django_rest_auth.urls')),
    path('', include('locations.urls')),
    path('', include('profiles.urls')),
    path('', include('reviews.urls')),
]