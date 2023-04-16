import requests
from Interfaces.ISearchesReader import ISearchesReader
from typing import List

class SearchesReader(ISearchesReader):
    def __init__(self):
        self._baseUrl = "https://www.daft.ie/property-for-rent/"
    
    def GetSearchLinks(self, fileName) -> List[str]:
        __file = open(fileName,mode='r')
        links = __file.read().split(" ")
        __file.close()
        return links


  