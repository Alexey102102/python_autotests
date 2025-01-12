import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = "34ec766f97dba5f2a92df0d80ab7e70b"
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.status_code)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_change = {
    "pokemon_id": f"{pokemon_id}",
    "name": "Momonsterr",
    "photo_id": -1
}

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.status_code)

body_addpokeball = {
    "pokemon_id": f"{pokemon_id}"
}

response_addpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_addpokeball)
print(response_addpokeball.status_code)