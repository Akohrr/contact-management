from django.shortcuts import render

from rest_framework import generics

from .models import Contact
from .serializers import ContactSerializer


class CreateContact(generics.CreateAPIView):
    serializer_class = ContactSerializer


class ListContact(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer