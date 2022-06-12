name_string = input("give everybody name with comma ")
names = name_string.split(",")
import random
name = len(names)
position = random.randint(0, name-1)
person = names[position]
print(person +' is going to pay')