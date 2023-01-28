posição = [1,2,3,4,5, 6, 7, 8, 9]
board = (f' {posição[0]} | {posição[1]} | {posição[2]} \n___|___|___\n'
         f' {posição[3]} | {posição[4]} | {posição[5]} \n___|___|___\n'
         f' {posição[6]} | {posição[7]} | {posição[8]} ')
print(board)

y = 1
x = 0
while (x < len(posição)):
    if y % 2 == 1:
        jogadorx = int(input("Jogador X em qual posição gostaria de jogar?"))
        y = y + 1
        for index, value in enumerate(posição):
            if value == jogadorx:
                posição[index] = "X"
                board = (f' {posição[0]} | {posição[1]} | {posição[2]} \n___|___|___\n'
                         f' {posição[3]} | {posição[4]} | {posição[5]} \n___|___|___\n'
                         f' {posição[6]} | {posição[7]} | {posição[8]} ')
                print(board)
    else:
        jogadorx = int(input("Jogador O em qual posição gostaria de jogar?"))
        y = y + 1
        for index, value in enumerate(posição):
            if value == jogadorx:
                posição[index] = "O"
                board = (f' {posição[0]} | {posição[1]} | {posição[2]} \n___|___|___\n'
                         f' {posição[3]} | {posição[4]} | {posição[5]} \n___|___|___\n'
                         f' {posição[6]} | {posição[7]} | {posição[8]} ')
                print(board)
    if posição[0] == "X" and posição[1] == "X" and posição[2] == "X":
        print("jogador X Ganhou!!!")
        break
    elif posição[3] == "X" and posição[4] == "X" and posição[5] == "X":
        print("jogador X Ganhou!!!")
        break
    elif posição[6] == "X" and posição[7] == "X" and posição[8] == "X":
        print("jogador X Ganhou!!!")
        break
    elif posição[0] == "X" and posição[3] == "X" and posição[6] == "X":
        print("jogador X Ganhou!!!")
        break
    elif posição[1] == "X" and posição[4] == "X" and posição[7] == "X":
        print("jogador X Ganhou!!!")
        break
    elif posição[2] == "X" and posição[5] == "X" and posição[8] == "X":
        print("jogador X Ganhou!!!")
        break
    elif posição[0] == "X" and posição[4] == "X" and posição[8] == "X":
        print("jogador X Ganhou!!!")
        break
    elif posição[2] == "X" and posição[4] == "X" and posição[6] == "X":
        print("jogador X Ganhou!!!")
        break
    elif posição[0] == "O" and posição[1] == "O" and posição[2] == "O":
        print("jogador O Ganhou!!!")
        break
    elif posição[3] == "O" and posição[4] == "O" and posição[5] == "O":
        print("jogador O Ganhou!!!")
        break
    elif posição[6] == "O" and posição[7] == "O" and posição[8] == "O":
        print("jogador O Ganhou!!!")
        break
    elif posição[0] == "O" and posição[3] == "O" and posição[6] == "O":
        print("jogador O Ganhou!!!")
        break
    elif posição[1] == "O" and posição[4] == "O" and posição[7] == "O":
        print("jogador O Ganhou!!!")
        break
    elif posição[2] == "O" and posição[5] == "O" and posição[8] == "O":
        print("jogador O Ganhou!!!")
        break
    elif posição[0] == "O" and posição[4] == "O" and posição[8] == "O":
        print("jogador O Ganhou!!!")
        break
    elif posição[2] == "O" and posição[4] == "O" and posição[6] == "O":
        print("jogador O Ganhou!!!")
        break

    x = x + 1