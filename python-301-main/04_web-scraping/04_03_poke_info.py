# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

import requests
from pprint import pprint
from pathlib import Path

BASE_URL = "https://pokeapi.co/api/v2/pokemon?limit=6"
request = requests.get(BASE_URL)

data = request.json()

def name_number_type():
    for i in data['results']:
        for k, v in i.items():
            print(v)

name_number_type()




# for k, v in data['results'][3].items():
#     print(k, v)

# pprint(data['results'][0]['name'])

# for name in data['results']:
#     for k, v in name.items():
#         print(k, v)
    
# for name in data['results']:
#     print(name['name'])
