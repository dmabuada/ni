from bs4 import BeautifulSoup
from django.contrib.sites.models import Site
from django.test import TestCase
from django.utils.text import slugify
from django.core.files.base import ContentFile

from product.models import Category
from product.models import Option, OptionGroup, Product, ProductImage
from product.modules.configurable.models import ConfigurableProduct


class SearchTestCase(TestCase):
    # fixtures = ['sample_data.yaml']

    def setUp(self):
        site = Site.objects.get_current()

        size_option_group = OptionGroup(
            site=site,
            name="size",
            sort_order=1
        )
        size_option_group.save()

        for j, size in enumerate([str(n) for n in range(0, 18, 2)]):
            variation = Option(
                name=size,
                value=size,
                sort_order=j,
                option_group=size_option_group
            )
            variation.save()

        dresses_category = Category(
            site=site,
            name="Dresses",
            slug="dresses",
            description="Dresses for all"
        )
        dresses_category.save()

        formal_dresses_category = Category(
            site=site,
            name="Formal Dresses",
            slug="formal",
            description="Formal dresses",
            parent=dresses_category
        )
        formal_dresses_category.save()

        test_dress = Product(
            site=site,
            name="Award Winner Gown",
            slug=slugify("Award Winner Gown"),
            description="Test dress used for testing search",
            featured=True
        )

        test_dress.save()

        test_dress.category.add(formal_dresses_category)

        dress_image = ProductImage(
            product=test_dress,
            picture=ContentFile(
                'x',
                name=slugify("Award Winner Gown")
            )
        )
        dress_image.save()

        test_dress.save()

        dress_variation = ConfigurableProduct(product=test_dress)
        dress_variation.save()
        dress_variation.option_group.add(size_option_group)
        dress_variation.save()
        dress_variation.create_all_variations()

    def test_search_page(self):
        """Assert that the search page comes back with a 200"""
        resp = self.client.get('/search/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.content)

    def test_filtering_size(self):
        """Assert that filtering on a size actually works"""
        # TODO: test filters on sizes that exist but have no results
        resp = self.client.get('/search/?size=30')
        soup = BeautifulSoup(resp.content)

        self.assertEqual(soup.find(id='search-results').text.strip().lower(), 'no results')

        resp = self.client.get('/search/?size=2')
        soup = BeautifulSoup(resp.content)
        search_results = soup.find(id='search-results').find_all('li')

        self.assertEqual(len(search_results), 1)

    def test_filtering_keywords(self):
        """Assert that filtering by keyword actually works"""
        resp = self.client.get('/search/?k=Award+Winner+Gown')
        soup = BeautifulSoup(resp.content)

        search_results = soup.find(id='search-results').find_all('li')
        self.assertEqual(len(search_results), 1)

        name = search_results[0].find(class_='name')
        self.assertEqual(name.contents[0], 'Award Winner Gown')
