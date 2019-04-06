__version__ = 0.3
__author__ = "Brandon Hiles"

# Default Modules
import argparse
import requests
import unittest

# Custom Dev Modules
from src.api.data_mining.parser import SiteMapParser
from src.api.data_mining.reuters import Reuters
from src.api.data_mining.wsj import WallStreetJournal
from src.api.data_mining.nyt import NewYorkTimes

from src.api.db.mongo import Mongo

# Test Modules
from test import *


# Basic Variables
host = 'localhost'
port = 27017
parser = argparse.ArgumentParser()
parser.add_argument("--coverage")

if __name__ == '__main__':

    # Analyze arguments passed to python script
    args = parser.parse_args()

    # If --coverage is passed, then run unit tests.
    # Syntax: python main.py --coverage=true
    if args.coverage:
        print("coverage turned on")
        runner = unittest.TextTestRunner()
        runner.run(site_availability_suite())
        runner.run(parser_suite())
        runner.run(reuter_suite())

    # Run main scripts
    reuters = SiteMapParser(website='https://www.reuters.com', host=host, port=port, collection='reuters')
    reuters.get_websites()
