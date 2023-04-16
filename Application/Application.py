from ast import Import
import sys
import os
sys.path.append(os.getcwd())

from Application.ListingProvider import ListingProvider
from Application.NewListingFinder import NewListingFinder



class Application:
    def __init__(self,
                 listingProvider,
                 newListingFinder):
        self.ListingProvider = listingProvider
        self.NewListingFinder = newListingFinder

    def Run(self):
        onlineListings = self.ListingProvider.Provide()
        self.NewListingFinder.DetectNewListings(onlineListings)
