import requests
from pprint import pprint


URL = 'https://swapi.dev/api/'

API_ENDPOINTS = {
    "people": "https://swapi.dev/api/people/",
    "planets": "https://swapi.dev/api/planets/",
    "films": "https://swapi.dev/api/films/",
    "species": "https://swapi.dev/api/species/",
    "vehicles": "https://swapi.dev/api/vehicles/",
    "starships": "https://swapi.dev/api/starships/"
}

response = requests.get(URL + API_ENDPOINTS + '/')
pprint(response.headers)

# with (open('output6.json', 'w', encoding='UTF-8') as file_out):

