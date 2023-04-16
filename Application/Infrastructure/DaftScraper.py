import requests
from typing import List
from bs4 import BeautifulSoup
import sys
sys.path.append("..")
from Interfaces.IDaftScraper import IDaftScraper

class DaftScraper(IDaftScraper):
    def __init__(self):
        self._baseUrl = "https://www.daft.ie/property-for-rent/"

    def GetLinks(self, url) -> List[dict]:
        __content = requests.get(self._baseUrl + url).content
        __soup = BeautifulSoup(__content)
        __script = __soup.find("script",
                              type = "application/json",
                             id = "__NEXT_DATA__")
        __scriptJson = json.loads(__script)
        listings = [val['listing'] for val in __scriptJson['props']['pageProps']['listings']]
        return listings

  