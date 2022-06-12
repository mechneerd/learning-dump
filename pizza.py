print("welcome to pizza deliveries")
size = input("what size of pizza you want? s,m or l?")
add_pepperoni = input("do you want pepperoni? y or n")
extra_cheese = input(" do you want extra cheese? y or n")
bill = 0
if size is 's':
    bill = 15
    #pepperoni
    if add_pepperoni is 'y':
       bill += 2
if size is 'm':
    bill = 20
    #pepproni
    if add_pepperoni is 'y':
       bill += 3 
if size is 'l':
    bill =25    
    #pepproni
    if add_pepperoni is 'y':
       bill += 3   
#cheese
if extra_cheese is 'y':
 bill += 1
 print(f'total bill is {bill}')
else:
 print(f'total bill is {bill}')