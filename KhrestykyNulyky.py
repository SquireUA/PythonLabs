from random import randint
# 
def show_bord(b):
    for i in range(13):
        if i == 0 or i == 4 or i == 8 or i == 12:
            print("+","-" * 7,"+","-" * 7,"+","-" * 7,"+")
        elif i == 2:
            print("|", " " * 2, b[0][0]," " * 2, "|", " " * 2, b[0][1]," " * 2, "|", " " * 2, b[0][2]," " * 2, "|")
        elif i == 6:
            print("|", " " * 2, b[1][0]," " * 2, "|", " " * 2, b[1][1]," " * 2, "|", " " * 2, b[1][2]," " * 2, "|")
        elif i == 10:
            print("|", " " * 2, b[2][0]," " * 2, "|", " " * 2, b[2][1]," " * 2, "|", " " * 2, b[2][2]," " * 2, "|")
        else:
            print("|", " " * 7, "|", " " * 7, "|", " " * 7, "|")

def khid(b):
    while True:
        r = randint(1, 9)
        for i in range(3):
            for j in range(3):
                if b[i][j] == r:
                    return r


def check(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2]:
            return True
        elif b[0][i] == b[1][i] == b[2][i]:
            return True

    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return True
    else:
        return False


board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

print("Let`s play")
count = 0
while True:
    if count == 1:
        print("You enter not number. Try again")
    if count == 2:
        print("You enter number out of range. Try again")
    if count == 3:
        print("This klitynka is zainyata")


    show_bord(board)

    for i in range(3):
        for j in range(3):
            if board[i][j] == 1 or board[i][j] == 2 or board[i][j] == 3 or board[i][j] == 4 or board[i][j] == 5 or board[i][j] == 6 or board[i][j] == 7 or board[i][j] == 8 or board[i][j] == 9:
                count = 4
                break
        if count == 4:
            break

    if count != 4:
        break
    try:
        zeros = int(input("Enter your move: "))
    except ValueError:
        count = 1
        continue

    if not (0 < zeros < 10):
        count = 2
        continue

    for i in range(3):
        for j in range(3):
            if board[i][j] == zeros:
                board[i][j] = 'O'
                count = 5
                break
        if count == 5:
            break

    if check(board):
        count = 7
        break
    elif count == 5:
        x = khid(board)
        for i in range(3):
            for j in range(3):
                if board[i][j] == x:
                    board[i][j] = 'X'
                    count = 6
                    break
            if count == 6:
                break
    else:
        count = 3
        continue

    if check(board):
        count = 8
        break

if count == 8:
    show_bord(board)
    print("I won!")
elif count == 7:
    show_bord(board)
    print("You won!")
else:
    print("Tie!")