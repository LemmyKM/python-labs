# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.



import requests
from pprint import pprint


url = "https://weatherapi-com.p.rapidapi.com/astronomy.json"

querystring = {"q":"Johannesburg"}

headers = {
	"x-rapidapi-key": "313ac4ab66msh88cd1f317e9a7eap1c128fjsn3bb8131661ce",
	"x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()
#pprint(data)

def moon_sun():
    print()
    print(data['location']['name'])
    print(data['location']['localtime'])
    for k, v in data['astronomy']['astro'].items():
        print(k,v)

moon_sun()