import json

#Sample json
userJSON = '{"First_name": "John", "last_name": "Doe", "age": 30}'

#Parse to dict
user = json.loads(userJSON)


# print(user)
# print(user['First_name'])

car = {'make': 'ford', 'model': 'mustang', 'year': 1970}
carJSON = json.dumps(car)

print(carJSON)