import json
import sys
from typing import List
import os

sys.path.append("..")

from Domain.Listing import Listing

class NewListingFinder:
    def __init__(self, jsonFileName : str):
        self.fileName = jsonFileName
        if os.path.exists(jsonFileName):
            with open(jsonFileName, "r") as file:
                self.Listings = json.load(file)
        else:
            self.Listings = dict()

    def DetectNewListings(self, onlineListings : List[Listing]) -> List[Listing]:
        currentListingIds = set(self.Listings.keys())
        onlineListingIds = set(listing._id for listing in onlineListings)
        newListings = onlineListingIds.difference(currentListingIds)

        if newListings:
            for listingId in newListings:
                newListing = next(l for l in onlineListings if l._id == listingId)
                self.Listings[listingId] = {'id': newListing._id, 'name': newListing._name, 'price': newListing._price}
            self.WriteListings(self.Listings)
        return list(newListings)

    def WriteListings(self, allListings : List[Listing]):
        with open(self.fileName, "w") as file:
            json.dump(allListings, file)


