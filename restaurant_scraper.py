from current_lunch_scraper import CurrentLunchScraper
from urllib.request import urlopen

class RestaurantScraper:

    def __init__(self, restaurants):
        self.restaurants = restaurants

    def get_first_lunch_table_by_class(self, page, element_class):
        self.soup = BeautifulSoup(page, "html.parser")
        all_tables = self.soup.find_all('table', class_=element_class)
        if len(all_tables) > 0:
            return all_tables[0]
        return None

    def get_current_lunch(self, key):
        if key in self.restaurants:
            restaurant = self.restaurants[key]
            page = urlopen(restaurant["url"])
            page_content = page.read())
            if restaurant["type"] == "table_class":
                return self.get_first_lunch_table_by_class(page_content,
                    restaurant["element_class"])
        return None
