from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Employee

class EmployeeAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345'
        )
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': '12345'
        })
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + response.data['access']
        )

    def test_create_employee(self):
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "department": "HR",
            "role": "Manager"
        }
        response = self.client.post('/api/employees/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_duplicate_email(self):
        Employee.objects.create(
            name="A", email="a@test.com"
        )
        response = self.client.post('/api/employees/', {
            "name": "B",
            "email": "a@test.com"
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_employee_404(self):
        response = self.client.get('/api/employees/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
