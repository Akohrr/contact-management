from django.urls import path

from . import views

app_name = 'contacts'


urlpatterns = [
    path('new', views.CreateContact.as_view(), name='new_contact'),
    path('all', views.ListContact.as_view(), name='list_contact'),
]
