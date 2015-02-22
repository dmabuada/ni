from django.test import TestCase


class HomePageTestCase(TestCase):

    def test_index(self):
        """Assert that the homepage works"""
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        # self.assertTrue(resp.url.endswith('/en-us/'))

    def test_ping(self):
        """Assert that the ping route comes back with a 200"""
        resp = self.client.get('/ping')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.content)
