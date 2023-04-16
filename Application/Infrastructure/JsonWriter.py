import json

class JsonWriter(IJsonWriter):
    def Write(listingsDict : dict,
              fileName : str) -> None:
        with open(fileName, "w") as f:
            json.dump(listingsDict, file)
        return None