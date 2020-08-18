num1 = eval(input('How many random numbers? '))
num2 = eval(input('lower limit of the numbers is: '))
num3 = eval(input('upper limit of the numbers is: '))
for i in range(1,num1+1):
 from random import randint
 x = randint(num2,num3)
 print('A random number between ',num2,' and ', num3,' is: ', x)
print ('these are ', num1, ' random numbers')
