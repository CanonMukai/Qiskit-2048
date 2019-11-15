
import numpy as np
import sys
import copy

ROW = 4
COLUMN = 4

def Display(board):
    print ("\n - - - - - - - - -")
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == '*':
                num = ' '
            else:
                num = board[i][j]
            if j == 0:
                print (" | %s" % num, end="")
            elif j%4 == 3:
                print (" | %s |" % num)
            else:
                print (" | %s" % num, end="")
        print (" - - - - - - - - -")

def Addition(a, b):
    return a + b

def Up(board):
    print ('up')
    for column in range(COLUMN):
        target = 0
        for row in range(1, ROW):
            if board[row][column] == '*':
                continue
            if board[target][column] == '*':
                board[target][column], board[row][column] = board[row][column], board[target][column]
            elif board[target][column] == board[row][column]:
                board[target][column] = Addition(board[target][column], board[row][column])
                board[row][column] = '*'
                target += 1
                if target == ROW - 1:
                    break
                continue
            else:
                target += 1
                if target == ROW - 1:
                    break
                target2 = target
                while target2 < row and board[target2][column] == '*':
                    if target2 == row - 1:
                        board[target][column], board[row][column] = board[row][column], board[target][column]
                        break
                    target2 += 1

def Down(board):
    print ('down')
    for column in range(COLUMN):
        target = ROW - 1
        for row in range(ROW - 2, -1, -1):
            if board[row][column] == '*':
                continue
            if board[target][column] == '*':
                board[target][column], board[row][column] = board[row][column], board[target][column]
            elif board[target][column] == board[row][column]:
                board[target][column] = Addition(board[target][column], board[row][column])
                board[row][column] = '*'
                target -= 1
                if target == 0:
                    break
                continue
            else:
                target -= 1
                if target == 0:
                    break
                target2 = target
                while target2 > row and board[target2][column] == '*':
                    if target2 == row + 1:
                        board[target][column], board[row][column] = board[row][column], board[target][column]
                        break
                    target2 -= 1

def Left(board):
    print ('left')
    for row in range(ROW):
        target = 0
        for column in range(1, COLUMN):
            if board[row][column] == '*':
                continue
            if board[row][target] == '*':
                board[row][target], board[row][column] = board[row][column], board[row][target]
            elif board[row][target] == board[row][column]:
                board[row][target] = Addition(board[row][target], board[row][column])
                board[row][column] = '*'
                target += 1
                if target == COLUMN - 1:
                    break
                continue
            # 
            else:
                target += 1
                if target == COLUMN - 1:
                    break
                target2 = target
                while target2 < column and board[row][target2] == '*':
                    if target2 == column - 1:
                        board[row][target], board[row][column] = board[row][column], board[row][target]
                        break
                    target2 += 1
                

def Right(board):
    print ('right')
    for row in range(ROW):
        target = COLUMN - 1
        for column in range(COLUMN - 2, -1, -1):
            if board[row][column] == '*':
                continue
            if board[row][target] == '*':
                board[row][target], board[row][column] = board[row][column], board[row][target]
            elif board[row][target] == board[row][column]:
                board[row][target] = Addition(board[row][target], board[row][column])
                board[row][column] = '*'
                target -= 1
                if target == 0:
                    break
                continue
            else:
                target -= 1
                if target == 0:
                    break
                target2 = target
                while target2 > column and board[row][target2] == '*':
                    if target2 == column + 1:
                        board[row][target], board[row][column] = board[row][column], board[row][target]
                        break
                    target2 -= 1

def Blank(board):
    blank_list = []
    for row in range(ROW):
        for column in range(COLUMN):
            if board[row][column] == '*':
                blank_list.append([row, column])
    return blank_list

def IsValid(board):
    for row in range(ROW):
        for column in range(COLUMN - 1):
            if board[row][column] == board[row][column + 1]:
                return True
    for column in range(COLUMN):
        for row in range(ROW - 1):
            if board[row][column] == board[row + 1][column]:
                return True
    return False

def OneStep(board, operation):
    old_board = copy.deepcopy(board)
    if operation == 'up':
        Up(board)
    elif operation == 'down':
        Down(board)
    elif operation == 'left':
        Left(board)
    elif operation == 'right':
        Right(board)
    if old_board == board:
        return 'Operation Error', board
    return Random2or4(board)

def Random2or4(board):
    blank_list = Blank(board)
    prob = np.random.random()
    if prob < 0.8:
        new_tile = 2
    else:
        new_tile = 4
    if len(blank_list) == 1:
        board[blank_list[0][0]][blank_list[0][1]] = new_tile
        if not IsValid(board):
            return 'Game Over', board
    else:
        random = np.random.randint(len(blank_list))
        blank = blank_list[random]
        board[blank[0]][blank[1]] = new_tile
    return 'Continue', board



board = [['*', '*', '*', '*'],
         ['*', '*', '*',  4 ],
         ['*', '*', '*', '*'],
         ['*',  2 , '*', '*']]
Display(board)
operation_list = ['up', 'down', 'left', 'right', 'q']
operation = ''
while operation != 'q':
    operation = input()
    if operation == 'q':
        print ('Quit')
        break
    if operation not in operation_list:
        print ('invalid operation')
        continue
    status, board = OneStep(board, operation)
    if status == 'Game Over':
        print (status)
        sys.exit()
    elif status == 'Operation Error':
        print ('`%s` is not available' % operation)
        Display(board)
    else:
        Display(board)

