from django.urls import path
from .views import ReviewList, ReviewDetail

urlpatterns = [
    path('reviews/', ReviewList.as_view()),
    path('reviews/<int:pk>/', ReviewDetail.as_view()),
]
