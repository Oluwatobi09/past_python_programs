num1 = eval(input('How many results? '))
num2 = eval(input('Lower limit for "x" value '))
num3 = eval(input('Upper limit for "x" value '))
num4 = eval(input('Lower limit for "y" value '))
num5 = eval(input('Upper limit for "y" value '))
for i in range(1,num1+1):
 from random import randint
 x = randint(num2,num3)
 y = randint(num4,num5)
 z = x**y
 print('the result of ',x,' to the power of ',y, 'is: ', z)

print('-------------------------------------')
name = input ('Enter your name: ')
for i in range(1,x):
 from random import randint
 x = randint(1,10)
 print ('Hello, ', name)
print('-------------------------------------')
num1 = eval(input('How many results? '))
from random import randec
x = randec(1,num1)
print(round(x,2))
