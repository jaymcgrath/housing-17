from django.test import TestCase, Client

# Create your tests here.
class TestAffordabilityEndpoint(TestCase):
    
    def setup(self):
        self.client = Client()

    def test(self):
        response = self.client.get('/housing_api/affordable/')

        self.assertEqual(response.status_code, 200)
