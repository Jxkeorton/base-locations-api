from django.urls import path
from .views import ContactList, ContactDetail

urlpatterns = [
    path('contact/', ContactList.as_view()),
    path('contact/<int:pk>/', ContactDetail.as_view()),
]
