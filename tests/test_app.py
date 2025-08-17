import unittest
import sys
import os

# Add the service directory to the path so we can import the app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../service'))

from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        """Set up test client before each test"""
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check_endpoint(self):
        """Test the main health check endpoint returns SERVICERUNNING"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), 'SERVICERUNNING')

    def test_health_endpoint(self):
        """Test the detailed health endpoint returns JSON with status"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'healthy')
        self.assertEqual(data['service'], 'running')

    def test_nonexistent_endpoint(self):
        """Test that non-existent endpoints return 404"""
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
