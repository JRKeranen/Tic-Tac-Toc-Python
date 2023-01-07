
class TTBoard:
    def base():
        #prints the board
        print(f'\n\n{p["1"]}{p["C"]}{p["2"]}{p["C"]}{p["3"]}\n{p["L"]}\n{p["4"]}{p["C"]}{p["5"]}{p["C"]}{p["6"]}\n{p["L"]}\n{p["7"]}{p["C"]}{p["8"]}{p["C"]}{p["9"]}\n\n')
    def win():
        #checks for a winner
        c = [[p['1'], p['2'], p['3']], [p['4'], p['5'], p['6']], [p['7'], p['8'], p['9']], [p['1'], p['4'], p['7']], [p['2'], p['5'], p['8']], [p['3'], p['6'], p['9']], [p['1'], p['5'], p['9']],[p['3'], p['5'], p['7']]]
        for e in c:
            if e == ['X','X','X']:
                stat = True
                return True
            if e == ['O','O','O']:
                stat = True
                return True
    def tie():
        #checks if there is a draw
        c = [[p['1'], p['2'], p['3']], [p['4'], p['5'], p['6']], [p['7'], p['8'], p['9']], [p['1'], p['4'], p['7']],
             [p['2'], p['5'], p['8']], [p['3'], p['6'], p['9']], [p['1'], p['5'], p['9']], [p['3'], p['5'], p['7']]]
        x = 0
        for e in c:
            if 'X' in e:
                if 'O' in e:
                    x += 1
            if x == 8:
                return True
    def option():
        #displays the options not in list form
        for n in options:
            print(f'{n} ')
    def score():
        print(f'numer of games:{d}\nX games Won:{dX}  O games won:{dO}\n')

stat = False

if __name__ == "__main__":
    n = '1'
    # d tracks total games, dX tracks X wins, dO tracks O wins
    d = 1
    dX = 0
    dO = 0
    while n != 'q':
        if n == 'n':
            #list of optional choices for turn
            options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            #dictionary that updates the tic tac to board
            p = {'1': '*', '2': '*', 'C': '|', '3': '*', 'L': '-----', '4': '*', '5': '*', '6': '*', '7': '*', '8': '*',
                 '9': '*'}
            #d tracks total games, dX tracks X wins, dO tracks O wins
            #d = 1
            #dX = 0
            #dO = 0

            while stat != True:
                for n in range(1, 1000):
                    #if and elif statement make sure players alternate turns
                    if (n % 2) == 1:
                        x = str(input(f'choose a position for X, The options are {options}:'))
                        p[x] = 'X'
                        options.remove(x)
                    elif (n % 2) == 0:
                        x = str(input(f'choose a position for O, The options are {options}:'))
                        p[x] = 'O'
                        options.remove(x)

                    # TTBoard.base() call function to display updated board
                    TTBoard.base()
                    #ends game when there is a winner
                    if TTBoard.win() == True:
                        if (n % 2) == 1:
                            print('X is winner winner chicken dinner\n')
                            dX += 1
                            TTBoard.score()
                            break
                        elif (n % 2) == 0:
                            print('O is winner winner chicken dinner!!\n')
                            dO += 1
                            TTBoard.score()
                            break
                        else:
                            print('ERROR')
                    if TTBoard.tie() == True:
                        print('GAME OVER! Draw!')
                        break
                break
            d += 1
        n = str(input('enter q to quit, enter n to continue:'))