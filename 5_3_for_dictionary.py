person = {'name':'egoing', 'address':'Seoul', 'interest':'Web'}
print(person['name'])

for key in person:
    print(key, person[key])

persons = [{'name':'egoing', 'address':'Seoul', 'interest':'Web'},
          {'name':'egoing', 'address':'Seoul', 'interest':'Web'},
          {'name':'egoing', 'address':'Seoul', 'interest':'Web'}]

print('==== persons ====')
for person in persons:
    for key in person:
        print(key, ':', person[key])
    print('-----------')



