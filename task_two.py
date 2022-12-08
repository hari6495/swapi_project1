"""
 "step 1: url of first movie1\n"
 "step 2:fetching details of films1\n"
 "step 3: convertit into json\n"
 "step 4: get list of url (names,vehicles,planets)\n"
 "step 5: iterate using for loop,call fetch data from each url\n"
 "step 6: get name from step5
 step 7: append names to list
 step 8: return name list
 """
from utils.fetch_data import fetch_data

url = "https://swapi.dev/api/films/1"
details = fetch_data(url)
planet = details.get('planets')
chara = details.get("characters")
vehi = details.get("vehicles")


def get_name(url_list):
    name = []
    for i in url_list:
        responce = fetch_data(i)
        name.append(responce.get('name'))
    return name


print(get_name(planet))

print(get_name(chara))
print(get_name(vehi))
