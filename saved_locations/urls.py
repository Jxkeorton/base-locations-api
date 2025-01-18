from django.urls import path
from .views import SavedLocationList, SavedLocationDetail

urlpatterns = [
    path('saved-locations/', SavedLocationList.as_view()),
    path('saved-locations/<int:pk>/', SavedLocationDetail.as_view()),
]
