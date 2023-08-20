import settings
import pygame

from node_state_enum import NodeState

class Node:
    def __init__(self, r: int, c: int, width: int, total_rows: int) -> None:
        self.row: int = r
        self.col: int = c
        self.x: int = r * width
        self.y: int = c * width
        self.state: NodeState = NodeState.WALKABLE
        self.color: tuple[int] = self.state.value
        self.neighbors: list[Node] = []
        self.width: int = width
        self.total_rows: int = total_rows
        
    def get_pos(self) -> tuple[int, int]:
        return self.row, self.col
    
    def is_closed(self) -> bool:
        return self.state == NodeState.CLOSED
    
    def is_open(self) -> bool:
        return self.state == NodeState.OPEN
    
    def is_bound(self) -> bool:
        return self.state == NodeState.BOUND
    
    def is_start(self) -> bool:
        return self.state == NodeState.START
    
    def is_end(self) -> bool:
        return self.state == NodeState.END
        
    def set_state(self, state: NodeState) -> None:
        self.state = state
        self.color = self.state.value
        
    def reset(self) -> None:
        self.set_state(NodeState.WALKABLE)
    
    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))
        
    def update_neighbors(self, grid: list[list[__build_class__]]) -> None:
        self.neighbors = []
        
        # Side nodes
        if self.row > 0 and not grid[self.row - 1][self.col].is_bound():
            self.neighbors.append(grid[self.row - 1][self.col]) # Append UP Node neighbor
            
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_bound():
            self.neighbors.append(grid[self.row + 1][self.col]) # Append DOWN Node neighbor
            
        if self.col > 0 and not grid[self.row][self.col - 1].is_bound():
            self.neighbors.append(grid[self.row][self.col - 1]) # Append LEFT Node neighbor
            
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_bound():
            self.neighbors.append(grid[self.row][self.col + 1]) # Append RIGHT Node neighbor
            
        # Corner nodes
        if self.row > 0 and not grid[self.row - 1][self.col].is_bound() and self.col > 0 and not grid[self.row][self.col - 1].is_bound() and not grid[self.row - 1][self.col - 1].is_bound():
            self.neighbors.append(grid[self.row - 1][self.col - 1]) # Append UP Left Node neighbor
        
        if self.row > 0 and not grid[self.row - 1][self.col].is_bound() and self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_bound() and not grid[self.row - 1][self.col + 1].is_bound():
            self.neighbors.append(grid[self.row - 1][self.col + 1]) # Append UP Right neighbor
        
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_bound() and self.col > 0 and not grid[self.row][self.col - 1].is_bound() and not grid[self.row + 1][self.col - 1].is_bound():
                self.neighbors.append(grid[self.row + 1][self.col - 1]) # Append Down Left Node neighbor
        
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_bound() and self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_bound() and not grid[self.row + 1][self.col + 1].is_bound():
            self.neighbors.append(grid[self.row + 1][self.col + 1]) # Append Down Right Node neighbor
