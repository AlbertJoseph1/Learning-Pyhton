#Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

#Use constructor
# person2 = dict(first_name='sara', last_name='Williams')

#Get value
print(person['first_name'])
print(person.get('last_name'))

#add key vaalue
person['phone'] = '555-555-555-555'

#Get dict keys
print(person.keys())

#Get dict items
print(person.items())

#Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

#Remove item
del(person['age'])
person.pop('phone')

#Clear
person.clear()

#Get length
print(len(person2))

#list of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 40}
]


print(people[1] ['name'])