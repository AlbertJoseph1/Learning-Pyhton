#Create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

#Single value needs a trailing comma
fruits2 = ('Apples',)

#Get a value
print(fruits[1])

#Delete a tuple
del fruits2

#Get length
print(len(fruits))


#Sets
#Create a set
fruits_set = {'Apples', 'Oranges', 'Grapes', 'Mango'}

#check if in set
print('Apples' in fruits_set)

#Add to set
fruits_set.add('Banana')

#Remove
fruits_set.remove('Grapes')

#Clear set
fruits_set.clear()

#Delete
del fruits_set

print(fruits_set)