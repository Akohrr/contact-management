from django.shortcuts import render

from rest_framework import generics

from .models import Contact
from .serializers import ContactSerializer


# POST Endpoint
class CreateContact(generics.CreateAPIView):
    serializer_class = ContactSerializer

# GET Endpoint
class ListContact(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# GET Endpoint
class ViewContact(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# PUT, PATCH Endpoint
class UpdateContact(generics.RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# DELETE Endpoint
class DeleteContact(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer