#! /usr/bin/env python

from lxml import html
from time import sleep
import requests, sys, os

def status():
    tot=int(os.path.getsize(os.path.realpath("guids.txt")))/37
    print("Wasted {} guids.".format(tot))

def main():
    while True:
        page = requests.get("http://wasteaguid.info/")
        tree = html.fromstring(page.content)
        guid = tree.xpath('//h1/text()')[1]
        with open("guids.txt", "a") as gfile:
            gfile.write(guid.rstrip("\n"))
        sleep(1)

if len(sys.argv) > 1:
    status()
else:
    main()
