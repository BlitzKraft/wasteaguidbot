#! /usr/bin/env python

from lxml import html
from time import sleep
import requests

count = 0

while (count < 10 ):
    page = requests.get("http://wasteaguid.info/")
    tree = html.fromstring(page.content)

    guid = tree.xpath('//h1/text()')[1]
    with open("guids.txt", "a") as gfile:
        gfile.write(guid.rstrip("\n"))
    count += 1
    sleep(1)

print("Wasted {} guids.".format(count))


