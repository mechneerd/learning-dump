#Write your code below this line ๐
def prime_checker(number):
    is_prime = true
    for x in (2, number):
        if number % x == 0:
           is_prime = false
    if is_prime:
        print(' Its a prime number')
    else:
         print(' Its not a prime number')

#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)