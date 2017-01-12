import ElementScraper from element_scraper

class ElementScraperHook:

    def __init__(self, element_hooks):
        self.element_hooks = element_hooks

    def get_element_of_key(self, key):
        if key in self.element_hooks:
            element_hook = self.element_hooks[key]
            page = urlopen(element_hook["url"])
            page_content = page.read())
            scraper = ElementScraper(page_content)
            return scraper.get_first_element_by_class(
                element_hook["element_type"], element_hook["element_class"])
        return None
