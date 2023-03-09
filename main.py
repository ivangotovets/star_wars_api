import logging
import re
import requests

from logging.handlers import RotatingFileHandler
from requests import RequestException
from sys import stdout

from exceptions import ConnectionError


URL = 'https://swapi.dev/api/'

API_ENDPOINTS = {
    "people": "https://swapi.dev/api/people/",
    "planets": "https://swapi.dev/api/planets/",
    "films": "https://swapi.dev/api/films/",
    "species": "https://swapi.dev/api/species/",
    "vehicles": "https://swapi.dev/api/vehicles/",
    "starships": "https://swapi.dev/api/starships/"
}

CONNECT_ERR_MSG = 'Connection error'
CONNECT_ERR_TEMP = 'Error connecting to endpoint'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=(
        RotatingFileHandler(
            filename='logger.log',
            maxBytes=40000000,
            backupCount=2
        ),
        logging.StreamHandler(stdout),
    )
)

NUM_RESULTS = 3

try:
    characters = requests.get(API_ENDPOINTS["people"] + '/')
    films = requests.get(API_ENDPOINTS["films"] + '/')

except RequestException as e:
    logging.error(e)
    raise ConnectionError(CONNECT_ERR_MSG)
characters = characters.json()['results']
films = films.json()['results']

with open('characters.json', 'w', encoding='UTF-8') as char_out:
    print('Characters', file=char_out)
    char_data = []
    for character in characters:
        episodes = []
        for film in character['films']:
            episodes.append(re.findall(r'\d+', film)[0])
        episodes = ', '.join(episodes)
        char_data.append([character["name"], episodes])

    for x, y in sorted(char_data, key=lambda x: (x[0], x[1])):
        char_out.write(f'{x}, episodes: {y}\n')
    print('\nFilm list', file=char_out)
    film_data = []
    for film in films:
        film_data.append([film["episode_id"], film["title"]])
    for x, y in sorted(film_data, key=lambda x:(x[0], x[1])):
        char_out.write(f'Episode {x}: {y}\n')
