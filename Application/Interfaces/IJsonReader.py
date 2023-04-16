import abc
import json

class IJsonReader:
    @abc.abstractmethod
    def Read(fileName: str) -> ListingsStore:
        raise NotImplementedError