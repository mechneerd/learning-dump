print("welcome to pizza deliveries")
size = input("what size of pizza you want? s,m or l?")
add_pepperoni = input("do you want pepperoni? y or n")
extra_cheese = input(" do you want extra cheese? y or n")
bill = 0
if size == 's':
    bill = 15
if size == 'm':
    bill = 20
if size == 'l':
    bill = 25
#pepperoni
if add_pepperoni == 'y':
    if size == 's':
     bill += 2
    else:
     bill += 3
#cheese
if extra_cheese == 'y':
 bill += 1
 print(f'total bill is {bill}')
else:
 print(f'total bill is {bill}')
