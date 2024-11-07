#create a function
def sayHello(name='Sam'):
    print(f'Hello {name}')

#Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

#Lambda function.

getSum = lambda num1, num2 : num1 + num2

print(getSum(10, 3))