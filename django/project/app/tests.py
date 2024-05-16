from django.test import TestCase

# Create your tests here.

class SignInTestCase(TestCase):
    def test_sign_in(self):
        data = {'email':'test@example.com','password':'password'}

        response = self.client.post(reversed('sign_in'),data)

        self.assertEqual(response.status_code,200)