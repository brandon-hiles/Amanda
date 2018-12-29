__version__ = 0.1
__author__ = "Brandon Hiles"

import unittest

from tests.api.test_SiteAvailability import SiteAvailabilityTestCases
from tests.api.test_parser import ParserTestCases

# Run Unit Tests

def site_availability_suite():
    suite = unittest.TestSuite()
    suite.addTest(SiteAvailabilityTestCases('test_checkReutersSiteAvailability'))
    suite.addTest(SiteAvailabilityTestCases('test_checkWSJSiteAvailability'))
    return suite

def parser_suite():
    suite = unittest.TestSuite()
    suite.addTest(ParserTestCases('test_grabSiteMapUrls'))
    suite.addTest(ParserTestCases('test_parseSiteMapUrls'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(site_availability_suite())
    runner.run(parser_suite())
