from django.urls import path

from . import views

app_name = 'contacts'


urlpatterns = [
    path('new', views.CreateContact.as_view())
]
