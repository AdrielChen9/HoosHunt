from django.test import TestCase
from django.template import Template, Context
from django.test.client import Client
from django.contrib.auth.models import User


from users.models import CustomUser
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


# User = get_user_model()

class LogInTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'secret'}
        self.user = get_user_model().objects.create_user(**self.user_data)

    def test_login(self):
        # send login data
        login_successful = self.client.login(
            username=self.user_data['username'],
            password=self.user_data['password']
        )
        self.assertTrue(login_successful, "Login failed")

        # Now, check if the user is logged in
        url = reverse('user')
        response = self.client.get(url)  # Replace with the actual protected page
        self.assertEquals(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        print("Login successful")


class GoogleMapsAPILoadingTestCase(TestCase):
    def test_google_maps_api_included(self):
        template = Template("{% include 'map.html' %}")
        rendered_template = template.render(Context({}))
        self.assertIn('https://maps.googleapis.com/maps/api/js', rendered_template)
