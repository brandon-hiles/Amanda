__version__ = 0.1
__author__ = "Brandon Hiles"

import unittest
import requests

from src.api.parser import SiteMapParser

class ParserTestCases(unittest.TestCase):

    """
    Testing SiteMapParser through reuters.com
    """

    @classmethod
    def setUp(self):
        self.website = 'https://www.reuters.com'
        self.parser = SiteMapParser(website=self.website)

    def test_grabSitemapUrls(self):

    	actual_data = self.parser.grab_sitemap_urls()
    	expected_data = [
    	'https://www.reuters.com/sitemap_index.xml'
    	'https://www.reuters.com/sitemap_news_index.xml'
    	'https://www.reuters.com/sitemap_video_index.xml'
    	'https://www.reuters.com/sitemap_market_index.xml'
    	]
    	self.assertEqual(expected_data, actual_data)

    @classmethod
    def tearDown(self):
        pass
