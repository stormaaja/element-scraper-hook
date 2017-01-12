import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(1, os.path.dirname(".."))

import unittest
from current_lunch_scraper import CurrentLunchScraper

class TestCurrentLunchScraper(unittest.TestCase):

    def test_table_with_class(self):
        f = open("tests/data/lunch_table.html", "r")
        page_content = f.read()
        f.close()
        scraper = CurrentLunchScraper(page_content)
        lunch = scraper.get_first_lunch_table_by_class("todayLunch")
        self.assertTrue("Chicken Vindaloo" in str(lunch))

if __name__ == "__main__":
    unittest.main()
