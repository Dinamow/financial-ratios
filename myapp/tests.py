from django.test import TestCase
from .models import Engine


# Create your tests here.
class MyTests(TestCase):
    
    def setUp(self):
        self.engine = Engine()
    
    def test_testing(self):
        """test the testing view"""
        response = self.client.get('/api/v1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'foo': 'bar'})
    
    def test_dates(self):
        """test the dates view"""
        response = self.client.get('/api/v1/dates/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['dates'], self.engine.get_dates())
    
    def test_balance(self):
        """test the balance view"""
        response = self.client.post('/api/v1/balance/')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'GET request required'})
        
        response = self.client.get('/api/v1/balance/?years=2022')
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(response.json(), {'result': 15})
