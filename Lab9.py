print("Приклад 1")

def mysplit(string):
    string = string.lstrip() + " "

    list_split = []

    if string.isspace() or string == '':
        return  list_split

    if string.find(" ") == -1:
        list_split.append(string)
        return list_split

    fnd_1 = 0
    fnd_2 = string.find(' ')

    while fnd_2 != -1:
        list_split.append(string[fnd_1:fnd_2])
        fnd_1 = fnd_2
        fnd_2 = string.find(' ', fnd_2 + 1)

    return list_split

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

print("Завдання 1")

# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
while True:
    zsuv = int(input("Enter number of zsuv(1-25): "))
    if zsuv >= 1 and zsuv <= 25:
        break
    else:
        print("Number is not correct. Please try again.")

for char in text:
    code = ord(char)
    if code >= 65 and code <= 90:
        code += zsuv
        if code > 90:
            code = 64 + (code - 90)

    if code >= 97 and code <= 122:
        code += zsuv
        if code > 122:
            code = 96 + (code - 122)
    cipher += chr(code)

print(cipher)





