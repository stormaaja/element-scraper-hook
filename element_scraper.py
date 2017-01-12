from bs4 import BeautifulSoup

from urllib.request import urlopen

class ElementScraper:

    def __init__(self, page_content, parser="html.parser"):
        self.soup = BeautifulSoup(page_content, parser)

    def get_all_elements_by_class(self, element_type, element_class):
        return self.soup.find_all(element_type, class_=element_class)

    def get_first_element_by_class(self, element_type, element_class):
        all_tables = self.get_all_elements_by_class(element_type, element_class)
        if len(all_tables) > 0:
            return all_tables[0]
        return None
