for i in range(3):
 print('Hello Welcome to Number Square bot')
 for i in range(3):
  num = eval(input('Enter a number: '))
  print ('The square of ', num,' is', num*num)
 print('Thank You. here are a couple of common and uncommon squares')
 for i in range(89,5,-3):
  print ('               ',i+1,end='')
  print ('',(i+1)*(1+i),sep='-')
 for i in range(8):
  print('               ','*'*(i+1))
 for i in range(4):
  print('               ','*'*2)
 for i in range(2):
  print('               ','*'*4)
print('Rerun to try again')

