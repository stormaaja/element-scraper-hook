#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer

from element_scraper_hook_handler import ElementScraperHookHandler
import config

class ScraperServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        # TODO validate token
        # TODO handle hook with path in thread
        self._set_headers()
        self.wfile.write("OK".encode())

    def handle_element_hook(self, path):
        handler = ElementScraperHookHandler(config.hooks)

def run(server_class=HTTPServer, handler_class=ScraperServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Starting httpd...")
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 1:
        run(port=config.server["port"])
    else:
        scraper = RestaurantScraper(config.restaurants)
        print(scraper.get_current_lunch(argv[1]))
