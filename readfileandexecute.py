filename = input('name')
content = input('enter content')
with open(f'{filename}.txt','w') as file:
    file.write(content)

open_file = input('open file y/n')
if open_file == 'y':
    with open(f'{filename}.txt','r') as file:
        print(file.read())
else:
    print('done')        