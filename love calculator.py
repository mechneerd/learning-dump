print('welcome to love calculator')
name1 = input('what is your name? \n')
name2 = input('what is their name? \n')
name1 = name1.lower()
name2 = name2.lower()
name3 = str(name1 + name2)
T=int(name3.count('t'))
R=int(name3.count('r'))
U=int(name3.count('u'))
E=int(name3.count('e'))
a = T+R+U+E
L=int(name3.count('l'))
O=int(name3.count('o'))
V=int(name3.count('v'))
E=int(name3.count('e'))
b = L+O+V+E
c = str(a + b)
d = int(c)
if d < 10 or d > 90:
  print(f' your score is {d} . you both are like coke & mentos')
elif d >= 40 and d<= 50:
  print(f'your score is {d}. your are alright together')
else:
    print(f'your score is {d}')