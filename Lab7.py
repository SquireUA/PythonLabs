# print("Приклад 1")
# results = (66, 77, 88)
#
# ave = sum(results) / len(results)
# max = max(results)
#
# print(f"Середнє значення: {ave} \nМаксимальне значення: {max}")
#
# print("Приклад 2")
#
# a = int(input("Введіть першу сторону : "))
# b = int(input("Введіть другу сторону : "))
# c = int(input("Введіть третю сторону : "))
#
# p = (a + b + c) / 2
#
# area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#
# tri = (a, b, c)
# print(f"Довжина трикутника: {tri} \nПроща трикутника: {area}")
#
# print("Приклад 3")
#
# t = tuple(input("Введіть елементи кортежу через кому: ").split(','))
#
# revers = t[::-1]
#
# print(t, "\n", revers)
import random

### Контрольні запитання

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.update({'d': 4})

print(my_dict)
print("Завдання 1")
p = []
for i in range(random.randint(1, 100)):
    p.append(random.randint(-100, 100))
t = tuple(p)
while True:
    try:
        n = float(input("Введіть число: "))
        break
    except ValueError:
        print("Це не число. Введіть знову")

result = [x for x in t if x < n]

print(result)

print("Завдання 2")

t = ("Hello", "my", "world")

t2 = ", ".join(t)

print(t2)

print("Завдання 3")

lib = {
    "Відьмак: меч призначення" : "Анджей Сапковський, 2016, 365 сторінок",
    "Космонафти з нашого будинку" : "Всеволод Нестайко, 2013, 347 сторінок",
    "Робінзон Крузо" : "Данієль Дефо, 2012, 272 сторінки"
}

name = input("Введіть назву книги: ")
count = 1
for i in lib.keys():
    if name == i:
        print(lib[i])
        count = 0
if count:
    print("Такої книги немає в бібліотеці")

print("Завдання 4")
students = {}
student_name = ("Круценко Дмитро",
                "Секретарюк Валерій",
                "Хань Євгеній")

student_info = ("Гейтер Рейфи",
                "Ігнорщік",
                "Лох")

for i in range(len(student_name)):
    students[student_name[i]] = student_info[i]

for name, info in students.items():
    print(name, " -> ", info)

print("Завдання 5")

phone = {"Діма":"2546456, 245767987",
        "Євген":"344574577, 3665867789",
        "Валерій": "0969482955, 465689090"}

while True:
    ask = input("Бажаєте додати номер?[y/n]: ")
    if ask == "y":
        while True:
            name = input("Введіть ім'я: ")
            if name not in phone.keys():
                print("Такого імені немає")
            else:
                try:
                    number = int(input("Введіть номер: "))
                    break
                except ValueError:
                    print("Ви ввели не номер. Спробуйте ще раз")
        phone[name] += f", {number}"
    elif ask == "n":
        break
    else:
       print("Я не знаю цієї команди спробуйте ще раз")

for name, number in phone.items():
    print(name, " -> ", number)
