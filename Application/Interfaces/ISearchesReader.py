import abc
from multiprocessing import Value
from typing import List

class ISearchesReader:
    @abc.abstractmethod
    def GetSearchLinks(self, fileName) -> List[str]:
        raise ValueError("Not implemented")
