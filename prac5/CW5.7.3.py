int_data = open('int_data.txt', 'r')
a = int_data.readline()
a = a.split()
for i in range(len(a)):
    a[i] = int(a[i])
b = []
for i in range(0, max(a)+1, 1):
    b.append(a.count(i))
number = 0
for i in range(0, len(b)):
    if b[i] != 0:
        number += 1
print(number)
