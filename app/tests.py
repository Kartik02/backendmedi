from django.test import TestCase
from django.urls import reverse

class APITest(TestCase):
    def test_submit_form(self):
        url = reverse('patient_create_view')
        data = {
            "name": "Test User",
            "email": "test@example.com",
            "phone": "1234567890",
            "city": "Test City",
            "address": "Test Address",
            "medicine": "Test Medicine",
            "prescription": None,
            "definition": "Test Definition"
        }
        response = self.client.post(url, data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 201)
