import time
import base64
import argparse

import requests
from bs4 import BeautifulSoup
import browsercookie

parser = argparse.ArgumentParser(
    description="Select browser to fetch cookies from.")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-c', action='store_true',
                   help="Pull cookies from Chrome.")
group.add_argument('-f', action='store_true',
                   help="Pull cookies from Firefox.")
group.add_argument('-a', action='store_true',
                   help="Pull cookies from all browsers.")
args = parser.parse_args()


def fetch_img(url):
    response = requests.get(url, stream=True)
    response.raw.decode_content = True
    return base64.b64encode(response.raw.read())


# Requests / browsercookie setup
url = 'https://www.youtube.com/playlist?list=WL'
# Set cookiejar from argument vector.
if args.c:
    cj = browsercookie.chrome()
elif args.f:
    cj = browsercookie.firefox()
else:
    cj = browsercookie.load()
r = requests.get(url, cookies=cj)

# BeautifulSoup setup
soup = BeautifulSoup(r.text, 'html.parser')

# YouTube
links = soup.find_all('tr', {'class': 'pl-video'})

with open('YT-WatchLater-Export {}.txt'.format(time.strftime("%Y-%m-%d-%H%M%S")), 'w', encoding='utf-8') as f:
    for link in links:
        # If deleted video, don't attempt to fetch image data (doesn't exist).
        if link.attrs['data-title'] == '[Deleted video]':
            f.write("{}\n".format(link.attrs['data-title']))
            f.write(
                "https://youtube.com{}\n".format(link.find('a').attrs['href'].split('&index=1&list=WL', 1)[0]))
            f.write('No image data.')
        # Else, fetch image data.
        else:
            f.write("{}\n".format(link.attrs['data-title']))
            f.write(
                "https://youtube.com{}\n".format(link.find('a').attrs['href'].split('&index=1&list=WL', 1)[0]))
            f.write('Image data:\n{}'.format(fetch_img("{}".format(
                link.find('img').attrs['data-thumb'].split('?', 1)[0]))))
        f.write("\n\n --------------------------------------------- \n\n")
