#!/usr/bin/env python

from __future__ import print_function

import sys
import urllib
import urllib2  # for the timeout err
import multiprocessing

import mechanize
from bs4 import BeautifulSoup

# from multiprocessing import dummy as multiprocessing


USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2244.0 Safari/537.36"


def category_url(cat):
    return 'https://www.renttherunway.com/dress/search/formality-{}'.format(cat)


br = mechanize.Browser()
br.addheaders = [('User-agent', USER_AGENT)]

# br.set_debug_http(True)
# br.set_debug_redirects(True)
# br.set_debug_responses(True)


def get_page_source(i):
    print('.', end='')
    sys.stdout.flush()

    browser = mechanize.Browser()
    browser.addheaders = [('User-agent', USER_AGENT)]
    browser.open(i)
    response = browser.response()

    if response.code != 200:
        return None

    try:
        return response.read()  # BeautifulSoup(response.read())
    except mechanize.RobotExclusionError as ree:
        print('Got a RobotExclusionError')
        return None
    except urllib2.URLError as urle:
        print('Timed out ' + str(urle))
        return None


def extract_dress_data(i):
    page = BeautifulSoup(i)
    print('.', end='')
    sys.stdout.flush()

    price_elem = page.find(class_='product-price-rental-label')
    price = str(price_elem.text.strip().replace('$', ''))

    image_url_elem = page.find('meta', {'name': 'sailthru.image.full'})
    image_url = image_url_elem.attrs['content']

    return {
        'name': page.find(class_='display-name').text.strip(),
        'price': price,
        'description': page.find(class_='product-details').text.strip(),
        'image-url': image_url
    }


def load_sample_data(url):
    br.open(url)
    soup = BeautifulSoup(br.response().read())
    links_to_dresses = soup.find_all(class_='item-link')

    full_links = []
    for link in links_to_dresses:
        full = 'http://' + br.request.host + urllib.quote(
            link.attrs['href'].encode('utf8')
        )

        full_links.append(full)

    pool = multiprocessing.Pool(4)
    print('Getting source...')
    pages = pool.map(get_page_source, full_links[:8])  # TODO: remove this limit
    print()
    pool.close()
    pool.join()

    pool = multiprocessing.Pool(8)
    print('Parsing and extracting...')
    dress_data = pool.map(extract_dress_data, [i for i in pages if i])
    print('\n\n')
    pool.close()
    pool.join()

    # TODO: make parallel. I got way too lazy at this point
    for i in dress_data:
        i['image-stream'] = urllib.urlopen(i['image-url'])

    # dress_data = []
    # for page_source in pages:
    # page = BeautifulSoup(page_source)
    # print('.', end='')
    # sys.stdout.flush()
    # this_dress = {}
    #     this_dress['name'] = page.find(class_='display-name').text.strip()
    #     dress_data.append(this_dress)
    # print()

    return dress_data


if __name__ == '__main__':
    import pprint

    pp = pprint.PrettyPrinter(indent=4)

    sample_data = [
        load_sample_data(category_url('black_tie')),
        # load_sample_data(category_url('cocktail')),
        # load_sample_data(category_url('night_out')),
        # load_sample_data(category_url('daytime'))
    ]

    pp.pprint(sample_data)

