from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Contact
from .serializers import ContactSerializer


# POST Endpoint
class CreateContact(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ContactSerializer

# GET Endpoint
class ListContact(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# GET Endpoint
class ViewContact(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# PUT, PATCH Endpoint
class UpdateContact(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# DELETE Endpoint
class DeleteContact(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer