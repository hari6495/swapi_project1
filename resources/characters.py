from resources.base import ResourceBase
from utils.fetch_data import fetch_data
class Characters(ResourceBase):
    def __init__(self):
        super().__init__()
        self.__relative_url="api/people"
        self.__character_range=[1,82]
    def get_count(self):
        plural_chracter_url=self.home_url+self.__relative_url
        var=fetch_data(plural_chracter_url)
        res=var.get('count')
        return res
    def get_resource_urls(self):
        print("this is code without understanding")




