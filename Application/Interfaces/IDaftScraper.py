import abc
from multiprocessing import Value
from typing import List
 
class IDaftScraper:
    @abc.abstractmethod
    def GetLinks(url: str) -> List[str]:
        raise ValueError("Not implemented")
