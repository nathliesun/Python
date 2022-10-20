import random

def pvp_mode(player1_candy, player2_candy):
    print ('PVP mode')
    candy= int(input('Введите количество конфет в стопке:'))
    while candy > 0:
        take1_candy = int(input('ПЕРВЫЙ игрок берет сколько конфет?:'))
        while take1_candy <= 0 or take1_candy >28:
            print('Брать можно только от 0 до 28 конфет')
            take1_candy = int (input('ПЕРВЫЙ игрок берет сколько конфет?:'))
        while take1_candy > candy:
            print('В стопке недостаточно конфет')
            take1_candy = int(input('ПЕРВЫЙ игрок берет сколько конфет?:'))
        else:
            if 0<=take1_candy <=28:
                player1_candy = player1_candy+take1_candy
                candy = candy-take1_candy
                print(f'У первого игрока: {player1_candy} конфет')
                print(f'конфет  стопке осталось: {candy} ')
                if candy == 0:
                    player1_candy = player1_candy+player2_candy
                    print(f'Первый игрок победил! /n C количеством конфет: {player1_candy} ')
                    print('Игра окончена! ')
                    return      
        take2_candy = int (input('  Второй игрок берет сколько конфет?:'))
        while take2_candy <= 0 or take2_candy >28:
            print('Брать можно только от 0 до 28 конфет')
            take2_candy = int (input('ВТОРОЙ игрок берет сколько конфет?:'))
        while take2_candy > candy:
            print('В стопке недостаточно конфет')
            take2_candy = int(input('ВТОРОЙ игрок берет сколько конфет?:'))
        else:
            if 0<=take2_candy <=28:
                player2_candy = player2_candy+take2_candy
                candy = candy-take2_candy
                print(f'У второго игрока: {player2_candy} конфет')
                print(f'конфет  стопке осталось: {candy} ')
                if candy == 0:
                    player2_candy = player2_candy+player1_candy
                    print(f'Второй игрок победил! /n C количеством конфет: {player2_candy} ')
                    print('Игра окончена! ')
                    return      

def pve_mode (comp_candy, player_candy):
    print('PvE mode')
    candy = int(input('Введи количество конфет в стопке:'))
    while candy > 0:
        take1_candy = random.randint(0, 28)
        if take1_candy > candy:
            take1_candy = candy
        print (f'Компьютер берет {take1_candy} конфет')
        comp_candy = comp_candy = take1_candy
        candy = candy-take1_candy
        print (f' У компьютера: {comp_candy} конфет')
        print (f' Конфет в стопке осталось: {candy} ')
        if candy == 0:
            player1_candy = comp_candy + player_candy
            print(f'Компьютер  победил! /n C количеством конфет: {player1_candy} ')
            print('Игра окончена! ')
            return  
        take2_candy = int(input('Игрок берет сколько конфет?'))
        while take2_candy <= 0 or take2_candy > 28:
            print('В стопке недостаточно конфет')
            take2_candy = int(input('Игрок берет сколько конфет?:'))
        else:
            if 0<=take2_candy <=28:
                player_candy = player_candy+take2_candy
                candy = candy-take2_candy
                print(f'У второго игрока: {player_candy} конфет')
                print(f'конфет  стопке осталось: {candy} ')
                if candy == 0:
                    player_candy = player_candy+comp_candy
                    print(f'Игрок победил! \n C количеством конфет: {player_candy} ')
                    print('Игра окончена! ')
                    return      


def mode_sel(mode):
    if mode == 1:
        player1_candy = 0
        player2_candy = 0
        pvp_mode (player1_candy, player2_candy)
    elif mode ==2:
        comp_candy =0
        player_candy = 0
        pve_mode(comp_candy, player_candy)
    else:
        print('Нет такого режима, выбери 1 или 2')

if __name__ == '__main__':
    modesel = int(input('Выбери режим игры: \n1- Против другого игрока \n2 - Против компьютера \n Выбор:'))
    mode_sel(modesel)
