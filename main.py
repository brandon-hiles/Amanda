
__author__ = "Brandon Hiles"

import requests

# Custom Modules
from src.api.data_mining.parser import SiteMapParser
from src.api.data_mining.reuters import Reuters
from src.api.data_mining.wsj import WallStreetJournal
from src.api.data_mining.nyt import NewYorkTimes

# Basic Variables
host = 'localhost'
port = 27017
