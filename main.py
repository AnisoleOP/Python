import random
a=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
def board():
    for i in range(3):
        for j in range(3):
            print(a[i][j],end='\t')
        print("\n")
def change_value_player(n):
    flag = -1
    for i in range(3):
        for j in range(3):
            if a[i][j] == n and a[i][j] != 'O':
                a[i][j] = 'X'
                flag = 0
    if flag == -1:
        k = int(input("Enter value of X again:"))
        change_value_player(k)
def change_value_computer(m):
    flag = -1
    for i in range(3):
        for j in range(3):
            if a[i][j] != 'X' and m == a[i][j]:
                a[i][j] = 'O'
                flag = 0
    if flag == -1:
        p = random.randint(1,9)
        change_value_computer(p)
def check_win():
    if a[0][0] == 'X' and a[0][1] == 'X' and a[0][2] == 'X':
        return 1
    elif a[0][0] == 'X' and a[1][0] == 'X' and a[2][0] == 'X':
        return 1
    elif a[1][0] == 'X' and a[1][1] == 'X' and a[1][2] == 'X':
        return 1
    elif a[0][1] == 'X' and a[1][1] == 'X' and a[2][1] == 'X':
        return 1
    elif a[2][0] == 'X' and a[2][1] == 'X' and a[2][2] == 'X':
        return 1
    elif a[0][2] == 'X' and a[1][2] == 'X' and a[2][2] == 'X':
        return 1
    elif a[0][0] == 'X' and a[1][1] == 'X' and a[2][2] == 'X':
        return 1
    elif a[2][0] == 'X' and a[1][1] == 'X' and a[0][2] == 'X':
        return 1
    elif a[0][0] == 'O' and a[0][1] == 'O' and a[0][2] == 'O':
        return 0
    elif a[0][0] == 'O' and a[1][0] == 'O' and a[2][0] == 'O':
        return 0
    elif a[1][0] == 'O' and a[1][1] == 'O' and a[1][2] == 'O':
        return 0
    elif a[0][1] == 'O' and a[1][1] == 'O' and a[2][1] == 'O':
        return 0
    elif a[2][0] == 'O' and a[2][1] == 'O' and a[2][2] == 'O':
        return 0
    elif a[0][2] == 'O' and a[1][2] == 'O' and a[2][2] == 'O':
        return 0
    elif a[0][0] == 'O' and a[1][1] == 'O' and a[2][2] == 'O':
        return 0
    elif a[2][0] == 'O' and a[1][1] == 'O' and a[0][2] == 'O':
        return 0
    else:
        flag = -1
        for i in range(3):
            for j in range(3):
                if a[i][j] != 'X' and a[i][j] != 'O':
                    flag = 0
        if flag == -1:
            return 2
while(1):
    print("PLAYER IS X AND COMPUTER IS O")
    board()
    n = int(input("Enter position of X:"))
    change_value_player(n)
    m = random.randint(1,9)
    change_value_computer(m)
    f = check_win()
    if f == 1:
        print("PLAYER WON")
        exit(f)
    elif f == 0:
        print("COMPUTER WON")
        exit(f)
    elif f == 2:
        print("GAME DRAW")
        exit(f)