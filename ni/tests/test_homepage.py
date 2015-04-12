from django.test import TestCase


class HomePageTestCase(TestCase):

    def test_index(self):
        """Assert that the homepage works"""
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        # self.assertTrue(resp.url.endswith('/en-us/'))

