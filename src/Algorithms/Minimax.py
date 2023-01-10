def minimax_search(state: Othello, depth: int) -> tuple:
    value, move = max_value(state, depth)
    return move
def max_value(state: Othello, depth: int) -> tuple:
    if state.is_terminal() or depth == 0:
        return state.utility(), None
    
    best_value = -float('inf')
    best_move = -float('inf')

    for action in state.actions():
        value, move = min_value(state.successor(action), depth - 1)
        if value > best_value:
            best_value = value
            best_move = action
    return best_value, best_move
    
def min_value(state: Othello, depth: int) -> tuple:
    if state.is_terminal() or depth == 0:
        return state.utility(), None
    
    best_value = float('inf')
    best_move = float('inf')

    for action in state.actions(): 
        value, move = max_value(state.successor(action), depth - 1)
        if value < best_value:
            best_value = value
            best_move = action
    return best_value, best_move