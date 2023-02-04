from time import time
from Othello import Othello
from Algorithms.Minimax import minimax_search
from Algorithms.Minimax_alpha_beta import minimax_search_alpha_beta
from Algorithms.heuristic_minimax import heuristic_minimax_search

class GameManager():
    def __init__(self):
        self.initial_state = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
        
    def start_game(self):
        t0 = time()
        othello = Othello(self.initial_state)
        print(othello)
        while not othello.is_terminal():
            
            #move = minimax_search(othello, 4)
            move = minimax_search_alpha_beta(othello, 4)
            #move = heuristic_minimax_search(othello, 4)
            othello.make_move(move)

            self.get_game_information(othello, move)
            
        self.get_winner(othello)
        t1 = time()
        print(f"Total time {(t1-t0)/60 if (t1-t0) >= 60 else (t1-t0)}")
        
    def get_winner(self, othello):
        if othello.utility() == 0:
            print("It's a draw!")
        elif othello.utility() == 1:
            print("Black wins!")
        else:
            print("White wins!") 
            
    def get_game_information(self, othello, move):
        player = "●" if othello.current_player == 2 else "○"
        if type(move) == tuple:
            print(f"Player {player} placed a tile at {move[0]} and {move[1]} tile(s) is(are) filliped.")
            print("Number of Whites:", othello.num_white)
            print("Number of Blacks:", othello.num_black)
            print(othello)
        else:
            print(f"{player} can not move so turn is missed.")