from django.test import TestCase
from bs4 import BeautifulSoup


class SearchTestCase(TestCase):
    fixtures = ['sample_data.yaml']

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
        resp = self.client.get('/search/?k=Award+Winner+Gown')
        soup = BeautifulSoup(resp.content)

        search_results = soup.find(id='search-results').find_all('li')
        self.assertEqual(len(search_results), 1)

        name = search_results[0].find(class_='name')
        self.assertEqual(name.contents[0], 'Award Winner Gown')
