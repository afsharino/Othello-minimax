def minimax_search_alpha_beta(state: Othello, depth: int) -> tuple:
        value, move = max_value_alpha_beta(state, -float('inf'), float('inf'), depth)
        return move
def max_value_alpha_beta(state: Othello, alpha: float, beta: float, depth: int) -> tuple:
    if state.is_terminal() or depth == 0:
        return state.utility(), None
    
    best_value = -float('inf')
    best_move = -float('inf')
    
    for action in state.actions():
        value, move = min_value_alpha_beta(state.successor(action), alpha, beta, depth - 1)
        if value > best_value:
            best_value = value
            best_move = action
            alpha = max(alpha, best_value)
        if best_value >= beta:
            return best_value, best_move
        
    return best_value, best_move
    
def min_value_alpha_beta(state: Othello, alpha: float, beta: float, depth: int) -> tuple:
    if state.is_terminal() or depth == 0:
        return state.utility(), None
    
    best_value = float('inf')
    best_move = float('inf')
    
    for action in state.actions():
        value, move = max_value_alpha_beta(state.successor(action), alpha, beta, depth - 1)
        if value < best_value:
            best_value = value
            best_move = action
            beta = min(beta, best_value)
        if best_value <= alpha:
            return best_value, best_move
    
    return best_value, best_move