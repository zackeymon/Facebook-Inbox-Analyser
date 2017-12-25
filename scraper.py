from bs4 import BeautifulSoup
import re


class Scraper:
    def __init__(self, file):
        self.soup = BeautifulSoup(file.read(), "lxml")
        self.datetime_pattern_matcher = re.compile(r"\w+,\s(\d+)\s(\w+)\s(\d+)\s\w+\s(\d+):(\d+)")

    def _get_all_messages(self):
        return self.soup.find_all("div", class_="message")

    def _get_datetime_components(self):
        pass

    def _reformat_datetime(self, datetime_string):
        pass