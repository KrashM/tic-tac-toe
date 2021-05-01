import game_state
import computer
import random
import math
import time

end_game = { 
    -1: 'X',
    1: 'O',
    0: 'TIE'
}

difficulty = 1
flip_flop = True

def get_difficulty():
    dif = int(input('Select difficulty:\nEasy = 1\nMedium = 2\nHard = 3\n'))
    global difficulty
    global flip_flop
    difficulty = dif
    if difficulty == 1:
        flip_flop = False
    elif difficulty == 3:
        flip_flop = True
    
def computer_turn():
    global difficulty
    global flip_flop
    #move = computer.minimax(9, True)[1]
    moves = game_state.get_possible_moves()
    move = None
    if flip_flop:
        move = computer.minimax_with_pruning(len(moves), -math.inf, math.inf, True)[1]
    else:
        move = moves[random.randint(0, len(moves) - 1)]
    if difficulty == 2:
        flip_flop = not flip_flop
    game_state.update_board(move, 'ai')
    game_state.show_game_state()

def player_turn():
    moves = game_state.get_possible_moves()
    selection = -1
    while selection not in moves:
        selection = int(input()) - 1
    game_state.update_board(selection, 'hn')
    game_state.show_game_state()

def game():
    get_difficulty()
    while(True):
        game_state.show_game_state()
        player_turn()
        result = game_state.check_for_win()
        if result != None: return end_game[result]

        time.sleep(1)
        computer_turn()
        result = game_state.check_for_win()
        if result != None: return end_game[result]

result = game()
if result == 'TIE':
    print(result)
else: print(result + ' WINS!!!')