#Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age =age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age += 1


#Extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age =age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and balnce is {self.balance}'

#Init user object
brad = User('Brad Teaversy', 'brad@gmail.com', 50)
# Init Customer
janet = Customer('Janet Johnson', 'Janet@yahoo.com', 35)

janet.set_balance(500)
print(janet.greeting())

brad.has_birthday()
print(brad.greeting())