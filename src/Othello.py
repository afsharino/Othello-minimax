from __future__ import annotations

class Othello:
    
    def actions(self) -> list:
        pass
    
    def successor(self, move) -> Othello:
        pass
    
    def is_terminal(self) -> bool:
        pass
    
    def utility(self) -> int:
        pass
    
    def is_cut_off(self, depth: int, depth_limit: int) -> bool:
        pass
    
    def heuristic(self) -> int:
        pass
        