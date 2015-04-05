from django.test import TestCase

class SearchTestCase(TestCase):

    def test_search(self):
        """Assert that search correctly filters comes back with a 200"""
        resp = self.client.get('/search/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.content)

