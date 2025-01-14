from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer

class ContactPermission(permissions.BasePermission):
    def has_permission(self, request):
        if request.method == 'POST':
            return True
        return request.user and request.user.is_superuser

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [ContactPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContactDetail(generics.RetrieveDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [ContactPermission]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.read:
            instance.read = True
            instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)