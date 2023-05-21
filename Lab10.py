print("Завдання 1")

word = input("Введіть слово: ")

symbols = input("Введіть набор символів: ")

i = 0

for char in symbols:
    if i < len(word):
        if char == word[i]:
            i += 1
    else:
        break

if i == len(word):
    print("Yes")
else:
    print("No")

print("Завдання 2")

# ПЕРШИЙ варіант

# Обчислює число "життя": суму цифр повної дати народження
while True:
    try:
        date = int(input("Введіть дату народження у форматі YYYYMMDD:"))
        break
    except ValueError:
        print("Ви не правильно ввели дату народження. спробуйте ще раз")


while True:
    sum = 0
    for simbol in date:
        sum += int(simbol)

    date = str(sum)

    if len(date) == 1:
        break

print(sum)

print("Завдання 3")

while True:
    try:
        number = int(input("Введіть ціле число: "))
        break
    except ValueError:
        print("Ви не ввели ціле число. Спробуйте знову.")

while True:
    mini = int(input("Введіть мінімальне значення: "))
    maxi = int(input("Введіть максимальне значення: "))
    if mini > maxi:
        print("мінімальне значення більше за максимальне. Спробуйте ще раз")
        continue
    if mini <= number <= maxi:
        print("Число ", number, " знаходиться в діапазоні(", mini, ",", maxi, ")")
        break
    else:
        print("Число ", number, "не знаходиться в діапазоні(", mini, ",", maxi, "). Спробуйте ще раз")



