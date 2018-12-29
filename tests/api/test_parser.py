__version__ = 0.1
__author__ = "Brandon Hiles"

import unittest
import datetime

from src.api.parser import SiteMapParser

class ParserTestCases(unittest.TestCase):

    """
    Testing SiteMapParser through reuters.com
    """

    @classmethod
    def setUp(self):
        self.website = 'https://www.reuters.com'
        self.parser = SiteMapParser(website=self.website)

    def test_grabSiteMapUrls(self):

        actual_data = self.parser.grab_sitemap_urls()
        expected_data = [
        'https://www.reuters.com/sitemap_index.xml',
        'https://www.reuters.com/sitemap_news_index.xml',
        'https://www.reuters.com/sitemap_video_index.xml',
        'https://www.reuters.com/sitemap_market_index.xml'
        ]
        self.assertEqual(expected_data, actual_data)

    def test_parseSiteMapUrls(self):
        actual_data = self.parser.parse_sitemap_data()[1][0]
        today_date = str(datetime.datetime.now().date()) # Returns year-month-day
        # We need yearmonthday (no -)
        split_date = today_date.split('-')
        today_date = ''.join(split_date)
        yesterday_date = str(int(today_date)-1)
        prefix = "https://www.reuters.com/sitemap_"
        expected_data = prefix + yesterday_date + "-" + today_date + ".xml"
        self.assertEqual(expected_data, actual_data)

    @classmethod
    def tearDown(self):
        pass
