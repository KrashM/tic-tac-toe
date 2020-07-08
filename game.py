import game_state
import computer
import math

end_game = { 
    -1: 'X', 
    1: 'O', 
    0: 'TIE'
}

def computer_turn():
    #move = computer.minimax(9, True)[1]
    move = computer.minimax_with_pruning(9, -math.inf, math.inf, True)[1]
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
    while(True):
        player_turn()
        result = game_state.check_for_win()
        if result != None: return end_game[result]

        computer_turn()
        result = game_state.check_for_win()
        if result != None: return end_game[result]

result = game()
if result == 'TIE':
    print(result)
else: print(result + ' WINS!!!')