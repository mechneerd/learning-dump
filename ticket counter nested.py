print(' ticket counter')
a = int(input('what is your height ? : '))
bill = 0
if a >= 120:
        print('you can ride')
        age = int(input('what is your age? : ')) 
        if age < 12:
            bill = 5
            print(' your ticket price is $5')
        elif age <= 18:
            bill = 7
            print('your tickect price is $7')
        else:
            if age > 18:
                if age >= 45 and age <= 55:
                    bill=0
                else:
                   bill = 12
                   print('your ticket is $12') 
        # to find photo fees
        photo = input(' do you want to take photo ? Y or N ')
        if photo == 'Y':
           bill += 3
           print(f"your total bill is ${bill}")
        else:
            print(f"your total bill is ${bill}")
else:
        print(' your are not allowed')