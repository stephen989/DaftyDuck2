import json
import sys
sys.path.append("..")
from Interfaces.IJsonReader import IJsonReader

class JsonReader(IJsonReader):
    def Read(fileName : str) -> ListingsStore:
        with open(fileName, "r") as file:
            listingStore = json.load(file)
        return listingStore
