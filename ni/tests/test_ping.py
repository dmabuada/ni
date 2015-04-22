from django.test import TestCase


class PingTestCase(TestCase):
    def test_ping(self):
        """Assert that the ping route comes back with a 200"""
        resp = self.client.get('/ping')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.content)

