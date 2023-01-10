from Othello import Othello

def heuristic_minimax_search(state: Othello, depth_limit: int) -> tuple:
        value, move = heuristic_max_value(state, -float('inf'), float('inf'), 0, depth_limit)
        return move
    
def heuristic_max_value(state: Othello, alpha: float, beta: float, depth: int, depth_limit: int) -> tuple:
    if state.is_cut_off(depth, depth_limit):
        return state.heuristic(), None
    
    best_value = -float('inf')
    best_move = -float('inf')
    
    for action in state.actions():
        value, move = heuristic_min_value(state.successor(action), alpha, beta, depth + 1, depth_limit)
        if value > best_value:
            best_value = value
            best_move = action
            alpha = max(alpha, best_value)
        if best_value >= beta:
            return best_value, best_move
        
    return best_value, best_move

def heuristic_min_value(state: Othello, alpha: float, beta: float, depth: int, depth_limit: int) -> tuple:
    if state.is_cut_off(depth, depth_limit):
        return state.heuristic(), None
    
    best_value = float('inf')
    best_move = float('inf')
    
    for action in state.actions():
        value, move = heuristic_max_value(state.successor(action), alpha, beta, depth + 1, depth_limit)
        if value < best_value:
            best_value = value
            best_move = action
            beta = min(beta, best_value)
        if best_value <= alpha:
            return best_value, best_move
    
    return best_value, best_move