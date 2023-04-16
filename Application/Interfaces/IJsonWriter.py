import abc

class IJsonWriter:
    @abc.abstractmethod
    def Write(listings : List[Listing],
              fileName: str) -> None:
        raise NotImplementedError