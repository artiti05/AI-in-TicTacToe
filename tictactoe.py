import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    return X if x_count<=o_count else O

def actions(board):
    s = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                s.add(tuple((i, j)))
    return s


def result(board, action):
    i, j = action
    
    if i < 0 or i >= 3 or j < 0 or j >= 3:
        raise Exception("Out of bound !!!")
    if board[i][j] is not EMPTY:
        raise Exception("Occupied Cell !!!")
    new_board = copy.deepcopy(board)
    ThePlayer = player(board)
    new_board[i][j] = ThePlayer
    
    return new_board

def winner(board):
    for row in board:
        if row == ['X', 'X', 'X']:
            return 'X'
        elif row == ['O', 'O', 'O']:
            return 'O'
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == 'X':
            return 'X'
        elif board[0][col] == board[1][col] == board[2][col] == 'O':
            return 'O'
        
    if board[0][0] == board[1][1] == board[2][2] == 'X':
        return 'X'
    elif board[0][0] == board[1][1] == board[2][2] == 'O':
        return 'O'
    
    if board[0][2] == board[1][1] == board[2][0] == 'X':
        return 'X'
    elif board[0][2] == board[1][1] == board[2][0] == 'O':
        return 'O'
    
    return None


def terminal(board):
    if winner(board) is not None or all(cell is not EMPTY for row in board for cell in row):
        return True
    else:
        return False
    
def utility(board):
    
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    
    if terminal(board):
        return None
    whos_turn = player(board)
    
    if whos_turn == X:
        best_v = -math.inf
        best_move = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_v:
                best_v = value
                best_move = action
        return best_move
    else:
        best_v = math.inf
        best_move = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_v:
                best_v = value
                best_move = action
        return best_move

def max_value(board):
    if terminal(board): #base case
        return utility(board)
    
    v = -math.inf
    for a in actions(board):
        v = max(v , min_value(result(board, a)))
    return v
        
        
def min_value(board):
    if terminal(board): #base case
        return utility(board)
    
    v = math.inf
    for a in actions(board):
        v = min(v, max_value(result(board, a)))
    return v
