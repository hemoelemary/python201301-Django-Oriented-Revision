import json
character = '''{
"name": "Luke Skywalker",
"height": "172",
"mass": "77",
"hair_color": "blond",
"skin_color": "fair",
"eye_color": "blue",
"birth_year": "19BBY",
"gender": "male",
"homeworld": "https://swapi.dev/api/planets/1/",
"films": [
    "https://swapi.dev/api/films/2/",
    "https://swapi.dev/api/films/6/",
    "https://swapi.dev/api/films/3/",
    "https://swapi.dev/api/films/1/",
    "https://swapi.dev/api/films/7/"
]}
'''
character = json.loads(character)
print(character['name'])

character['name']='HamodaElemary'
print(json.dumps(character))

"""
json.loads() str => dict
json.dumps() dict => str
"""