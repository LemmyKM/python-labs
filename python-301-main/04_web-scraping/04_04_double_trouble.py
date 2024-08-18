# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.

import requests
from pprint import pprint

def astronomy():
    url = "https://weatherapi-com.p.rapidapi.com/astronomy.json"

    querystring = {"q":"Johannesburg"}

    headers = {
	    "x-rapidapi-key": "313ac4ab66msh88cd1f317e9a7eap1c128fjsn3bb8131661ce",
	    "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()
    locat = data['location']['name']
    time = data['location']['localtime']
    sun_moon = data['astronomy']['astro']
    #pprint(data)

    with open('sun_moon_air.txt', mode='a', encoding='utf-8') as sma:
        sma.write(locat)
        sma.write('\n')
        sma.write(time)
        sma.write('\n')
        for k, v in sun_moon.items():
            sma.write(f"{k} : {v}'\n'")
        sma.write('\n')

astronomy()


def air_quality():
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q":"Johannesburg","aqi":"yes"}
    headers = {
        "x-rapidapi-key": "313ac4ab66msh88cd1f317e9a7eap1c128fjsn3bb8131661ce",
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    #pprint(data)

    data2 = data['current']['air_quality']
    data3 = str(data2)

    with open('sun_moon_air.txt', mode='a', encoding='utf-8') as sma:
        data4 = data3.replace('co', 'Carbon Monoxide (ug/m3)')
        data5 = data4.replace('no2', 'Nitrogen Dioxide (ug/m3)')
        data6 = data5.replace('o3', 'Ozone (ug/m3)')
        data7 = data6.replace('so2', 'Sulphur Dioxide (ug/m3)')
        data8 = data7.replace('{', "")
        data9 = data8.replace('}', "")
        data10 = data9.replace("'", "")
        data11 = data10.replace(',', '\n')
        sma.write(data11)
        sma.write('\n')

air_quality()