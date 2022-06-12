def greet():
    print(' hi angela')
    print(' how r you')
    print(' r u fine?')
greet()

def greet_with_name(x):
    print(f'hi {x}' )
    print(f' how r you {x}' )
    print(f' r u fine? {x}')

greet_with_name('prasanth')

def greet_with_loc(x,y):
    print(f'hi {x}')
    print(f'i live in {y}')
    
greet_with_loc(y = 'tnj',x ='prasanth')