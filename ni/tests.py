from django.test import TestCase


class HomePageTestCase(TestCase):

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(resp.url.endswith('/en-us/'))