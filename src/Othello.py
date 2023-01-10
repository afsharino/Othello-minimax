from __future__ import annotations

class Othello:
    def __init__(self, board:list):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.current_player = 1
        self.num_black = 2
        self.num_white = 2
        
    def actions(self) -> list:
        """The set of legal moves in given state."""
        # List of available actions 
        list_of_actions = []
        
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == 0:
                    captured = self.get_captured_tiles(row, col)
                    if captured:
                        list_of_actions.append(((row, col), len(captured)))
        return list_of_actions
    
    def get_captured_tiles(self, row: int, col: int) -> list:
        """get captured tiles in all 8 direction"""
        captured = []
        
        for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0),
                                       (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            captured.extend(self.get_captured_tiles_in_direction(row, col, row_offset, col_offset))
        
        return captured
    
    def get_captured_tiles_in_direction(self, row: int, col: int, row_offset: int, col_offset: int) -> list:
        """get captured tiles in given direction"""
        captured = []
        
        row += row_offset
        col += col_offset
        
        while not self.is_out_of_bound(row, col):
            if self.board[row][col] == 0:
                return []
            
            if self.board[row][col] == self.current_player:
                return captured
            
            captured.append((row, col))
            
            row += row_offset
            col += col_offset
            
        return []
    
    def is_out_of_bound(self, row, col):
        """Return False if the given position is on the board, True otherwise"""
        return not (0 <= row < self.rows and 0 <= col < self.cols)
    
    def make_move(self, move:tuple) -> None:
        """make move and update number of tiles for each player and flip tiles"""
        if type(move) == tuple:
            position, num_captured = move
            row, col = position
            self.board[row][col] = self.current_player
            if self.current_player == 1:
                self.num_black += 1 + num_captured
                self.num_white -= num_captured
            else:
                self.num_white += 1 + num_captured
                self.num_black -= num_captured

            # Capture tiles
            for r, c in self.get_captured_tiles(row, col):
                self.board[r][c] = self.current_player

            self.current_player = 2 if self.current_player == 1 else 1
        else:
            self.current_player = 2 if self.current_player == 1 else 1
    
    def successor(self, move) -> Othello:
        """Defines the state resulting from taking given action on given state."""
        board = [row[:] for row in self.board]
        new_game = Othello(board)
        new_game.turn = self.current_player
        new_game.num_black = self.num_black
        new_game.num_white = self.num_white
        new_game.make_move(move)
        return new_game
    
    def is_terminal(self) -> bool:
        """A terminal test, which is true when the game is over and false otherwise."""
        if self.num_black + self.num_white == self.rows * self.cols:
            return True
        
        elif not bool(self.actions()):
            self.current_player = 2 if self.current_player == 1 else 1
            if not bool(self.actions()):
                return True
            self.current_player = 2 if self.current_player == 1 else 1
        
        else:
            return False
    
    def utility(self) -> int:
        """Defines the final numeric value to player when the game ends in terminal state"""
        if self.num_black == self.num_white:
            return 0
        return 1 if self.num_black > self.num_white else -1
    
    def is_cut_off(self, depth: int, depth_limit: int) -> bool:
        """Returns True if the search should be terminated at the current depth, False otherwise."""
        if depth == depth_limit:
            return True
        if self.is_terminal():
            return True
        return False
    
    def heuristic(self) -> int:
        """estimates a state’s utility"""
        black_tiles = self.num_black if self.current_player == 1 else self.num_white
        white_tiles = self.num_white if self.current_player == 1 else self.num_black
        black_corner, white_corner = (0,0)
        for tile in [self.board[0][0], self.board[0][-1], self.board[-1][0], self.board[-1][-1]]:
            if tile == 1:
                black_corner += 1
            elif tile == 2:
                white_corner += 1
            else:
                continue

        score = (black_tiles + 2 * black_corner) - (white_tiles - 2 * white_corner)
        if score > 0:
            return 1
        elif score == 0:
            return 0
        else:
            return -1
    
    def __str__(self) -> str:
        """Print board"""
        counter = 0
        s = "  0  1  2  3  4  5  6  7  \n"
        for row in self.board:
            s += f"{counter}"
            for cell in row:
                s += " ● " if cell == 1 else " ○ " if cell == 2 else " - "
            s += "\n"
            counter += 1
        return s