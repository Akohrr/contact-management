from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User
from contacts.models import Contact


class BaseTestClass(APITestCase):
    def setUp(self):
        self.username = 'testusername'
        self.password = 'aodhoihdaldhfl'
        self.data = {
            'username': self.username,
            'password': self.password
        }
        self.user = User.objects.create_user(
            username=self.username, password=self.password, email='testemail@test.com')
        self.token_url = reverse('token_obtain_pair')
        token_resp = self.client.post(self.token_url, self.data)
        self.assertEqual(token_resp.status_code, status.HTTP_200_OK)
        self.access_token = token_resp.data['access']


# test for GET request
class TestListContactView(BaseTestClass):
    url = reverse('contacts:list_contact')

    def test_unauthenticated_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_request_with_authenticated_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# test for POST request
class TestCreateContactView(BaseTestClass):
    url = reverse('contacts:new_contact')

    def test_unauthenticated_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_request_with_authenticated_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_request_with_authenticated_user(self):
        test_data = {
            'name': 'testname',
            'address': 'testaddress',
            'owner': self.user.id,
            'work_phone': '2348123456789'
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.post(self.url, test_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestUpdateContactView(BaseTestClass):
    def setUp(self):
        super().setUp()
        test_data = {
            'name': 'testname',
            'address': 'testaddress',
            'owner': self.user,
            'work_phone': '2348123456789'
        }
        self.contact = Contact.objects.create(**test_data)
        self.url = reverse('contacts:update_contact', kwargs={'pk': self.contact.id})

    def test_unauthenticated_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # get requests allow you to view details of a contact
    def test_get_request_with_authenticated_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # PUT request allow you to modify contact instance
    def test_put_request_with_authenticated_user(self):
        new_test_data = {
            'name': 'modifiedname',
            'address': 'modifiedaddress',
            'owner': self.user.id,
            'work_phone': '23400000000'
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.put(self.url, new_test_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)# after database has been modified throught PUT  and PATCH request, aserrt that new data is in database
        obj = Contact.objects.get(name='modifiedname')        
        self.assertIsInstance(obj, Contact)
        self.assertEqual(obj.name, 'modifiedname')

    # PATCH request allow you to modify contact instance
    def test_patch_request_with_authenticated_user(self):
        new_test_data = {
            'name': 'modifiedname',
            'address': 'modifiedaddress',
            'owner': self.user.id,
            'work_phone': '23400000000'
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.patch(self.url, new_test_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # after database has been modified throught PUT  and PATCH request, aserrt that new data is in database
        obj = Contact.objects.get(name='modifiedname')        
        self.assertIsInstance(obj, Contact)
        self.assertEqual(obj.name, 'modifiedname')


# test for DELETE request
class TestDeleteContactView(BaseTestClass):
    def setUp(self):
        super().setUp()
        test_data = {
            'name': 'testname',
            'address': 'testaddress',
            'owner': self.user,
            'work_phone': '2348123456789'
        }
        self.contact = Contact.objects.create(**test_data)
        self.url = reverse('contacts:delete_contact', kwargs={'pk': self.contact.id})

    def test_get_request_with_authenticated_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_request_with_authenticated_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

