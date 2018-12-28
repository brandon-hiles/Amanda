__version__ = 0.1
__author__ = "Brandon Hiles"

# Primary Libraries
import os
import sys
import time
import unittest
import zlib

# Third Party Libraries
import requests
import bs4

# Custom Modules
from src.api.parser import SiteMapParser
from src.api.reuters import Reuters
from src.api.wsj import WallStreetJournal

host = 'localhost' # Location for MongoDB
port = 27017 # Port for MongoDB
num_websites = 1000 # Specify number of websites, you want to parse

reuters = Reuters(host=host, port=port)
wsj = WallStreetJournal(host=host, port=port)

reuters_sites = reuters.store_websites(upper_bound=num_websites)
wsj_sites = wsj.store_websites(upper_bound=num_websites)