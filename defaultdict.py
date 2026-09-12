obj = {
    'name':'Hamoda',
    'Age':19,
}
name = obj.get(obj['name'],'Mohamed')
print(name)

text = '''
{

"name":"Hamoda"
}
'''
import json
p=json.loads(text)
print(p['name'])
print(p.get('age',19),p.get('age',None))
p['name']='hamoda'
print(json.dumps(p))
