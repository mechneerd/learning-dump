print('welcome to calculator')
operation = input('which operation do you want to do? add,sub,mult,divide: ')
a = input ('input ur 1st number: ')
b = input ('input ur 2nd number: ')
a = int(a)
b = int(b)
if operation == 'add':
 print(a+b)
if operation == 'sub':
 print(a-b)
if operation == 'mult':
 print(a*b)
if operation == 'divide':
 print(a/b)
