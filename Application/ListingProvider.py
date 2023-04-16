import sys
from typing import List
from Application.Interfaces.ISearchesReader import ISearchesReader
from Application.Interfaces.IDaftScraper import IDaftScraper
from Application.Infrastructure.DaftScraper import DaftScraper
from Application.Infrastructure.SearchesReader import SearchesReader
from Application.Domain.Listing import Listing

class ListingProvider:
    def __init__(self,
        daftScraper : IDaftScraper,
        searchesReader : ISearchesReader,
        daftLinksFile : List[str]         
                 ):
        self.DaftScraper = daftScraper
        self.DaftLinks = searchesReader.GetSearchLinks(fileName=daftLinksFile)

    def Provide(self) -> List[Listing]:
        listingList = list()
        for link in self.DaftLinks:
            onlineListings =  self.DaftScraper.GetLinks(link)
            for onlineListing in onlineListings:
                listingList.append(
                                   Listing(
                                            onlineListing['id'],
                                            onlineListing['title'],
                                            onlineListing['abbreviatedPrice']
                                           )
                                )
        return listingList
print(0)