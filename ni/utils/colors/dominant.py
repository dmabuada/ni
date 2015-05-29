#!/usr/bin/env python

from __future__ import print_function

from PIL import Image
import scipy
import scipy.misc
import scipy.cluster

NUM_CLUSTERS = 5


def dominant_colors(file_path):
    im = Image.open(file_path)
    im = im.resize((150, 150))  # optional, to reduce time
    ar = scipy.misc.fromimage(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2])

    codes, dist = scipy.cluster.vq.kmeans(ar.astype(float), NUM_CLUSTERS)

    vecs, dist = scipy.cluster.vq.vq(ar, codes)  # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))  # count occurrences

    to_sort = zip(counts, codes)

    def get_frequency(n):
        return n[0]

    by_frequency = sorted(to_sort, key=get_frequency, reverse=True)
    print(by_frequency)
    return [tuple(row[1]) for row in by_frequency]


if __name__ == '__main__':
    import sys

    try:
        image_file_path = sys.argv[1]
    except IndexError as ie:
        sys.exit(1)

    print(dominant_colors(image_file_path))
