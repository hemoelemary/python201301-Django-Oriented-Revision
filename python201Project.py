import requests
while True:
    name = input('name:')
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    if name=='break':
        break
    get = requests.get(url)
    print(get.json())
    