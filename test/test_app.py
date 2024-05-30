import unittest
from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_search(self):
        response = self.app.get('/search?query=McDonald%27s&start_date=2023-01-01&end_date=2023-01-10')
        self.assertEqual(response.status_code, 200)
        self.assertIn('articles', response.json)

    def test_missing_parameters(self):
        response = self.app.get('/search')
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
