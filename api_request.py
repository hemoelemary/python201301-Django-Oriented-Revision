# import requests

# req = requests.get('https://swapi.dev/api/planets/1/')
# print(req.status_code)

# import requests
# import time
# while True:
#     req = requests.get('https://swapi.dev/api/planets/1/')
#     if req.status_code!=200:
#         #email me if request not
#         pass
#     time.sleep(3)

import requests
req = requests.get('https://swapi.dev/api/planets/1/')
print(req.status_code)
print(req.json())
print(req.json()['name'])
for film in req.json()['films']:
    print(requests.get(film).json()['title'])

#getting film titls 