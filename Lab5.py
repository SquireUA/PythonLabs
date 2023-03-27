list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)
print("Завдання 1")
array = [1, 2, 3, 4, 5]
while 1:
    ch = int(input("Enter number of element you want to change (from 1 to 5): "))
    if ch >= 1 & ch <= 5:
        break
    else:
        print("Number isn`t in range from 1 to 5. Try again")
number = int(input("Enter number you want change to:"))

array[ch-1] = number

del array[-1]

print(array)

print("Завдання 2")

array = [3, 8, 12, 1, 5, -1]

print(array)

for i in range(len(array) - 1):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)

print("Завдання 3")

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

rep = []
for i in range(len(my_list)):
    if my_list[i] not in rep:
        rep.append(my_list[i])
my_list = rep[:]
print("The list with unique elements only:")
print(my_list)

print("Завдання 4")

chess = [["_" for i in range(8)] for j in range(8)]

chess[0][0], chess[0][-1], chess[-1][0], chess[-1][-1] = 'tura', 'tura','tura','tura'

print(chess)