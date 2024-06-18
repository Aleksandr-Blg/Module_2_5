import random
list1 = random.randint(3, 20)
list2 = 'список пар: '
print(list1)
for i in range(1, list1):
    for j in range(i, list1):
        if list1 % (i + j) != 0 or j == i:
            continue
        list2 = list2 + ' ' +  str(i) + '+' + str(j)
else:
    print(list2)