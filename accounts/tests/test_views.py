from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User


class TestAuthentication(APITestCase):
    def setUp(self):
        self.username = 'testusername'
        self.password = 'aodhoihdaldhfl'
        self.data = {
            'username': self.username,
            'password': self.password
        }
        self.user = User.objects.create_user(
            username=self.username, password=self.password, email='testemail@test.com')
        self.url = reverse('token_obtain_pair')

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_invalid_user(self):
        response = self.client.post(
            self.url, data={'username': 'wrongusername', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_user(self):
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # acccording to the docs: https://github.com/davesque/django-rest-framework-simplejwt#usage a valid post request would give access and refresh parameters
    def test_token_generated_sucessfully(self):
        response = self.client.post(self.url, data=self.data)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)
