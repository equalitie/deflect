from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

class APITestCase(TestCase):

    def setUp(self):
        test_pwd = 'testpassword'
        test_admin = User.objects.create_superuser(
            'testuser', 'testuser@example.com', test_pwd)
        self.client = Client()
        self.client.login(username=test_admin.username, password=test_pwd)

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
