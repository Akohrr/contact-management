import os

from django.db import models

# local imports
from accounts.models import User


def contact_picture_directory_path(instance, filename):
    upload_to = 'conatcts/{0}/{1}'.format(instance.owner.username, instance.name)
    ext = filename.split('.')[-1]
    filename = '{0}.{1}'.format(instance.id, ext)
    return os.path.join(upload_to, filename)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    work_phone = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to=contact_picture_directory_path, blank=True)

    def __str__(self):
        return self.name
