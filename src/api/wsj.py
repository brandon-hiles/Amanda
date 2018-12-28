__version__ = 0.1
__author__ = "Brandon Hiles"

import bs4
import requests
from pymongo import MongoClient

from src.api.parser import SiteMapParser

class WallStreetJournal(SiteMapParser):

    """
    WallStreetJournal is an interface for parsing data from wsj.com

    Initialization Parameters:
    1. Host: Specify Where the Databse is. If local DB: host='localhost'
    2. Port: Used to specify the port instance of the db. If local DB
    port=27017
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = MongoClient(host, port)
        super().__init__(website='https://www.wsj.com')

    def _extract_title(self, website):
    	# Use meta data to grab title
        
        element = super().grab_elements(website)
        tag = element[0].find("meta",  property="og:title")
        if type(tag) is bs4.element.Tag:
            return tag['content']
        if type(tag) is  None:
            return ""

    def _extract_description(self, website):
    	# Use meta to grab a description of article

        element = super().grab_elements(website)
        tag = element[0].find("meta",  property="og:description")
        if type(tag) is bs4.element.Tag:
            return tag['content']
        if type(tag) is  None:
            return ""
    
    def _extract_type(self, website):
        # Use meta to grab type of article

        element = super().grab_elements(website)
        tag = element[0].find("meta",  property="og:type")
        if type(tag) is bs4.element.Tag:
            return tag['content']
        if type(tag) is  None:
            return ""

    def store_websites(self, upper_bound):

        db = self.client['news']
        wsj = db['wsj']

        urls = super().get_websites()
        for index in range(0, upper_bound+1):
            website = requests.get(urls[index]).content.decode('utf-8')
            query = {
                 "title" : self._extract_title(website),
                 "description" : self._extract_description(website),
                 "type" : self._extract_type(website),
                 "url" : urls[index]
            }
            wsj.insert_one(query).inserted_id