# Create a list
numbers = [1,2,3,4,5,6]
fruits = ['Apples', 'Grapes', 'Oranges', 'Pears']

#Use a constructor
# numbers2 = list((1,2,3,4,5,6))

#Get a value
print(fruits[1])

#Get the length
print(len(fruits))

#Append to list (adding to the end of the list)
fruits.append('Mangos')

#Remove form list
fruits.remove('Grapes')

#Insert into position
fruits.insert(2, 'Strawberries')

#change a value
fruits[0] = 'Blueberries'

#Remove from position with pop
fruits.pop(2)

#Reverse list
fruits.reverse()

#Sort list
fruits.sort()

#Reverse Sort
fruits.sort(reverse=True)

print(fruits)
