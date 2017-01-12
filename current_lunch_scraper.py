from bs4 import BeautifulSoup

class CurrentLunchScraper:

    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")

    def get_first_lunch_table_by_class(self, element_class):
        all_tables = self.soup.find_all('table', class_=element_class)
        if len(all_tables) > 0:
            return all_tables[0]
        return None
