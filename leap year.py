a = int(input('what year you want to check : '))
if a%4 == 0:
    if a%100 == 0:
        if a%400== 0:
            print('it is a leap year')
        else:
            print('not a leap year')
    else:
        print('leap year')
else:
    print('not a leap year')