import pyttsx3
#рисуем игровое поле
def draw_board (board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|",board[1+i*3],"|",  board[2+i*3], "|" )
        print("-" * 13)

#Запрашиваем ходы
def take_input(player_token):
    valid = False
    while not valid:
        engine = pyttsx3.init()
        engine.say("куда поставим твой символ?")
        engine.runAndWait()
        player_answer = input("Куда поставим" + player_token+"?")
        try:
            player_answer = int(player_answer)
        except:
            engine = pyttsx3.init()
            engine.say("Вводить нужно числа от 1 до 9")
            engine.runAndWait()
            print("Вводить нужно числа от 1 до 9.")
            continue
        if 1 <= player_answer <=9:
            if str(board[player_answer-1]) not in "XO":
                board[player_answer-1] = player_token
                valid = True
            else:
                engine = pyttsx3.init()
                engine.say("Эта клетка уже занята")
                engine.runAndWait()
                print('Эта клетка уже занята')
        else:
            engine = pyttsx3.init()
            engine.say("Вводить нужно числа от 1 до 9")
            engine.runAndWait()
            print('Вводить нужно числа от 1 до 9.')

#Проверка победы
def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] ==board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter %2 ==0:
            take_input("X")
        else:
            take_input("0")
        counter +=1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                engine = pyttsx3.init()
                engine.say("Ты победил!")
                engine.runAndWait()
                print( tmp, "Победил!")
                win = True
                break
        if counter ==9:
            engine = pyttsx3.init()
            engine.say("Ничья!")
            engine.runAndWait()
            print("Ничья!")
            break
    draw_board(board)

if __name__ == '__main__':
    engine = pyttsx3.init()
    engine.say("Давай поиграем в игру крестики- нолики")
    engine.runAndWait()
    print("Игра крестики-нолики для двух игроков")
    board = list(range(1, 10))

    main(board)
    input("Нажмите ентер для входа")