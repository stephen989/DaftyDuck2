import sys
import time
from Application.Application import Application
from Application.ListingProvider import ListingProvider
from Application.NewListingFinder import NewListingFinder
from Infrastructure.DaftScraper import DaftScraper
from Application.Infrastructure.SearchesReader import SearchesReader
class Program:
    def __init__(self, timeDelay = 30):
        daftLinksFile = "daftLinks.txt"
        jsonFileName = "daftListings.json"
        searchesReader = SearchesReader()
        self.ListingProvider = ListingProvider(
            DaftScraper(),
            searchesReader,
            daftLinksFile
            )
        self.NewListingFinder = NewListingFinder(jsonFileName) 
        self.Application = Application(
            self.ListingProvider,
            self.NewListingFinder
                                       )

        while True:
            self.Application.Run()
            time.sleep(timeDelay)

if __name__ == "__main__":
    print("Here")
    Program()