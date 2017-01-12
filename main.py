#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer

from restaurant_scraper import RestaurantScraper
import config

class ScraperServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        scraper = RestaurantScraper(config.restaurants)
        current_lunch = scraper.get_current_lunch(self.path.replace("/", ""))
        if current_lunch is not None:
            self.wfile.write(current_lunch.encode())
        else:
            self.wfile.write("Not found".encode())

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
