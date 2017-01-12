from current_lunch_scraper import CurrentLunchScraper
from urllib.request import urlopen

class RestaurantScraper:

    def __init__(self, restaurants):
        self.restaurants = restaurants

    def get_current_lunch(self, key):
        if key in self.restaurants:
            restaurant = self.restaurants[key]
            page = urlopen(restaurant["url"])
            scraper = CurrentLunchScraper(page.read())
            if restaurant["type"] == "table_class":
                return scraper.get_first_lunch_table_by_class(restaurant["element_class"])
        return None
