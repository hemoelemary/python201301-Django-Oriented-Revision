#test
#context manager

#------READING FILE---------
with open('C:\\Users\\AdminOS\\kalobdocs\\Python201301\\python201301-Django-Oriented-Revision\\file.txt','r') as file:
    print(file.read())


with open('C:\\Users\\AdminOS\\kalobdocs\\Python201301\\python201301-Django-Oriented-Revision\\README.md','r') as readme:
    content = readme.read()

print(content)

#------CREATING FILE----------
with open('write_file.txt','w') as file:
    #overwriting
    file.write('hello from python 201 a second time')

with open('write_file.txt','a') as file:
    file.write('\n \tappended text')

with open('file.txt','a') as f:
    f.write('hello')

with open('file.txt','r') as f:
    print(f.read())


#-------------read_mult_lines---------
with open('emails.txt','r') as emails:
    emails=emails.readlines()
for email in emails:
    if 'hotmail' in email:
        print(email.rstrip())    
    



with open('emails.txt','r') as file:
    emails2 = file.readlines()
for email in emails2:
    # print(email)
    if 'hotline' in email:
        print(email)


# 'r' read 'w' write 'a' append

