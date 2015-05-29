
import os

from ni.utils.colors.get_colors import colorz
from ni.utils.colors.dominant import dominant_colors as dc
from ni.utils.colors import find_nearest_color


from django.test import TestCase


class NearestColorTestCase(TestCase):
    def setUp(self):
        TEST_ROOT = os.path.abspath(os.path.dirname(__file__))
        self.yellow = os.path.join(TEST_ROOT, 'test_data', 'MNL75.jpg')

    def test_nearest_color(self):
        """
        Assert that the find_nearest_color function is able to accurately
        determine a nearest color
        """
        dominant_colors = colorz(self.yellow)
        closest_colors = [find_nearest_color(rgb) for rgb in dominant_colors]

        dominant_colors = dc(self.yellow)
        closest_colors = [find_nearest_color(rgb) for rgb in dominant_colors]
        print closest_colors
