a = input('u r first name')
b = input('u r last name')


def format_name(f_name, l_name):
    x = f_name.title()
    y = l_name.title()
    return f"{x} {y}"


j = format_name(a, b)
print(j)    
    