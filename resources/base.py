from abc import ABC,abstractmethod
class ResourceBase():
    resources=["planets","people","vehicles","starships","films"]
    def __init__(self):
        self.home_url="https://swapi.dev/"
    @abstractmethod
    def get_count(self):
        pass
    @abstractmethod
    def get_resource_urls(self):
        pass

