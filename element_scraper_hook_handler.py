import ElementScraper from element_scraper

class ElementScraperHookHandler:

    def __init__(self, element_hooks):
        self.element_hooks = element_hooks

    def get_element_of_hook(self, hook_path):
        if hook_path in self.element_hooks:
            element_hook = self.element_hooks[hook_path]
            page = urlopen(element_hook["element_url"])
            page_content = page.read())
            scraper = ElementScraper(page_content)
            return scraper.get_first_element_by_class(
                    element_hook["element_identifier_type"],
                    element_hook["element_class"])
        return None
