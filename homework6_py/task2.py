#рисуем игровое поле
from email.mime import nonmultipart


def draw_board (board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|",board[1+i*3],"|",  board[2+i*3], "|" )
        print("-" * 13)

#Запрашиваем ходы
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"?")
        try:
            player_answer = int(player_answer)
        except:
            print("Вводить нужно числа от 1 до 9.")
            continue
        if 1 <= player_answer <=9:
            if str(board[player_answer-1]) not in "XO":
                board[player_answer-1] = player_token
                valid = True
            else:
                print('Эта клетка уже занята')
        else:
            print('Вводить нужно числа от 1 до 9.')

#Проверка победы
def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    if len(list(filter(lambda x: board[x[0]] == board[x[1]] == board[x[2]], win_coord))) == 0:
        return False
    else:
        return True

def main(board):
    XO = lambda num: "X" if num %2 == 0 else "O"
    counter = 0
    win = False
    while not win:
        draw_board(board)
        take_input(XO(counter))
        if counter > 4:
            if check_win(board):
                print(XO(counter), "Победил!")
                win = True
                break
        if counter ==9:
            print("Ничья!")
            break
        counter +=1
    draw_board(board)

if __name__ == '__main__':
    print("Игра крестики-нолики для двух игроков")
    board = list(range(1, 10))

    main(board)
    input("Нажмите ентер для входа")

