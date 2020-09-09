import sys

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, force_authenticate

class APITestCase(TestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_superuser(
            'testuser', 'testuser@example.com', 'testpassword')
        self.token = Token.objects.create(user=self.user).key
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_api_auth_token(self):
        # Issue a GET request.
        response = self.client.post('/api-token-auth/', {
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check if token is present in JSON body
        self.assertIn('token', response.json())


    def test_edge_query(self):
        # Print info
        response = self.client.get('/api/edge/list', {
            'dnet': 'test'
        })

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
