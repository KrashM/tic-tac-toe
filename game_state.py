board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

players = {
    'hn': 'X',
    'ai': 'O'
}

def check_for_win():
    if board[0] == board[1] and board[1] == board[2]:
        if board[0] == players['hn']: return -1
        else: return 1
    if board[3] == board[4] and board[4] == board[5]: 
        if board[3] == players['hn']: return -1
        else: return 1
    if board[6] == board[7] and board[7] == board[8]: 
        if board[6] == players['hn']: return -1
        else: return 1
    if board[0] == board[3] and board[3] == board[6]: 
        if board[0] == players['hn']: return -1
        else: return 1
    if board[1] == board[4] and board[4] == board[7]: 
        if board[1] == players['hn']: return -1
        else: return 1
    if board[2] == board[5] and board[5] == board[8]: 
        if board[2] == players['hn']: return -1
        else: return 1
    if board[0] == board[4] and board[4] == board[8]: 
        if board[0] == players['hn']: return -1
        else: return 1
    if board[2] == board[4] and board[4] == board[6]: 
        if board[2] == players['hn']: return -1
        else: return 1
    flag = True
    for i in range(9):
        if board[i] != players['hn'] and board[i] != players['ai']:
            flag = False
            break
    if flag: return 0
    return None

def get_possible_moves():
    free = []
    for i in range(9):
        if board[i] != players['hn'] and board[i] != players['ai']: free.append(i)
    return free

def update_board(i, player):
    board[i] = players[player]

def undo(i):
    board[i] = i + 1

def show_game_state():
    import os
    os.system('cls')
    print("{}|{}|{}\n-|-|-\n{}|{}|{}\n-|-|-\n{}|{}|{}".format(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))

def evaluate():
    score = 0
    score += evaluate_line(0, 1, 2)
    score += evaluate_line(3, 4, 5)
    score += evaluate_line(6, 7, 8)
    score += evaluate_line(0, 3, 6)
    score += evaluate_line(1, 4, 7)
    score += evaluate_line(2, 5, 8)
    score += evaluate_line(0, 4, 8)
    score += evaluate_line(2, 4, 6)
    return score

def evaluate_line(cell_1, cell_2, cell_3):
    score = 0
 
    if board[cell_1] == players['ai']: score = 1
    elif board[cell_1] == players['hn']: score = -1
 
    if board[cell_2] == players['ai']:
        if score == 1: score = 10
        elif score == -1: return 0
        else: score = 1
    elif board[cell_2] == players['hn']:
        if score == -1: score = -10;
        elif score == 1: return 0
        else: score = -1

    if board[cell_3] == players['ai']:
        if score > 0: score *= 10
        elif score < 0: return 0
        else: score = 1
    elif board[cell_3] == players['hn']:
        if score < 0: score *= 10
        elif score > 1: return 0
        else: score = -1

    return score