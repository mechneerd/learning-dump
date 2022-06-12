print('welcome to rock , paper ,scissor')
rock = (''' -------
         -----------''')
paper =('''  +++++++++++++''')
scissors = (''' &&&&&&''')

choice = int(input('type 0 for rock ,1 for paper ,2 for scissors'))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

import random
pc_chose = random.randint(0, 2)
pc_chose = int(pc_chose)
if pc_chose == 0:
    print(rock)
elif pc_chose == 1:
    print(paper)
else:
    print(scissors)
x = (str(choice)+str(pc_chose))
if x == '11' or x == '22' or x == '00':
    print('DRAW')
elif x == '10' or x == '02' or x == '21':
    print('you won')
elif x == '01' or x == '20' or x == '12':
    print('pc won')

