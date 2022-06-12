# hangman
import random
l = ['car','bike','flight']
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
f = random.choice(l)
print(f)
#print(len(f)*'_ ')
# this helps to create ' _ '
b = []
for r in f:
    b += "_"

# this will fill the '_' with letters if right

while '_' in b:
      a = input("guess a letter ").lower()
      ch = a
      if ch in f:
         for k in range(len(f)):
             r = f[k]
             if r == a:
                b[k] = r
          # letter doesn't match
      elif ch not in f:
                n = 0
               
                if n < 0 :
                   print(stages[n])
                   
      print(''.join(b))
      # if all filled this print message
      if '_' not in b:
          print('player won')

      
    
    
    