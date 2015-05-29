# TODO: silver, gold, pattern

from ni.utils.colors.get_colors import colorz as dominant_colors

COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'orange': (255, 127, 0),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'gray': (127, 127, 127),
    'pink': (255, 127, 127),
    'purple': (127, 0, 255),
    # 'cream': (244, 238, 219),
    'brown': (126, 79, 2)
}


def distance(left, right):
    return sum((l - r) ** 2 for l, r in zip(left, right)) ** 0.5


class NearestColorKey(object):
    def __init__(self, goal):
        self.goal = goal

    def __call__(self, item):
        return distance(self.goal, item[1])


def find_nearest_color(rgb_tuple):
    return min(COLORS.items(), key=NearestColorKey(rgb_tuple))
