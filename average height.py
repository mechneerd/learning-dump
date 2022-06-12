std_height = input('input list of height').split()
for n in range(0, len(std_height)):
    std_height[n] = int(std_height[n])
print(std_height)
total=0
for s in std_height:
    total +=s
print(total)
no_of_height = 0
for q in std_height:
    no_of_height += 1
print(no_of_height)
print(round(total/no_of_height))