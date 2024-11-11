#Open a file
myFile = open('myfile.txt', 'w')

#Get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

#Write to file
myFile.write('I love Ice cream')
myFile.write(' and Pizza')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I alos like pilau')
myFile.close()

#Read from a file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)