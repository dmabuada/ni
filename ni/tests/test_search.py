from django.test import TestCase

class SearchTestCase(TestCase):

    def test_search_page(self):
        """Assert that the search page comes back with a 200"""
        resp = self.client.get('/search/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.content)

    def test_filtering_size(self):
        """Assert that filtering on a size actually works"""
        pass

    def test_filtering_keywords(self):
        """Assert that filtering by keyword actually works"""
        pass

