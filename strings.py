name = 'Albert'
age = 54

#Concatenate.
# print('hello, my name is '+ name + ' and I am ' + str(age))

#String Formatting.

#Agrumnets by position.
# print('My name is {name} and I am {age}'.format(name=name, age=age))

#F-Strings
# print(f'Hello, my name is {name} and I am {age}')

#String Methods

s = 'hello world'

#Capitalize string
print(s.capitalize())

#Make all uppercase
print(s.upper())

#Make all lower
print(s.lower())

#Swap case
print(s.swapcase())

#Get Length
print(len(s))

#Replace
print(s.replace('world', 'everyone'))

#Count
sub = 'h'
print(s.count(sub))

#Starts with
print(s.startswith('hello'))

#Ends with
print(s.endswith('d'))

#spilt into last
print(s.split())

#Find Position
print(s.find('r'))

#Is all aphanumeric
print(s.isalnum())

#Is all alphabetic
print(s.isalpha())

#Is all numeric
print(s.isnumeric())