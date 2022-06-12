print('welcome to rock , paper ,scissor')
rock = (''' -------
         -----------''')
paper =('''  +++++++++++++''')
scissors = (''' &&&&&&''')

choice = int(input('type 0 for rock ,1 for paper ,2 for scissors'))
if choice == 0:
    print('you chose rock ' +rock)
elif choice == 1:
    print('you chose paper' +paper)
else:
    print('you chose scissor ' +scissors)

import random
pc_chose = random.randint(0, 2)
pc_chose = int(pc_chose)
if pc_chose == 0:
    print('pc chose rock ' + rock)
elif pc_chose == 1:
    print('pc chose paper' + paper)
else:
    print('pc chose scissor ' + scissors)
x = (str(choice)+str(pc_chose))
if x == '11' or x == '22' or x == '00':
    print('Draw')
elif x == '10' or x == '02' or x == '21':
    print('you won')
elif x == '01' or x == '20' or x == '12':
    print('pc won')

