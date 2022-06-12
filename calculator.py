#ADD
def add(n1, n2):
    return n1+n2
#SUB
def sub(n1, n2):
    return n1-n2
# multiply
def multi(n1, n2):
    return n1*n2
#divide
def div(n1, n2):
    return n1/n2

operation = {'+' : add,
              '-' : sub,
              '*' : multi,
              '/' : div
              }
def calc():
    num1 = float(input('type the 1st number : '))
    for x in operation:
          print(x)
    loop = True
    while loop:
          choice = input('pick an operation : ')
          num2 = float(input('type the another number : ' ))
          result = operation[choice](num1, num2)
          print(f'{num1} {choice} {num2} = {result}')
          k = input('do you want to continue "yes" or "no" : ')
          if k == 'yes':
              result = num1
          else:
              loop = False
              calc()

calc()



      
          