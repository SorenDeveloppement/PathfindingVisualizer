import pygame
import settings

from node import Node
from node_state_enum import NodeState
from astar_pathfinding import astar_algorithm

pygame.init()
pygame.display.set_caption("A* pathfinding - SorenDev")
screen: pygame.Surface = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

def create_grid(r: int, w: int) -> list[list[Node]]:
    grid: list[list[Node]] = []
    gap: int = w // r
    
    for i in range(r):
        grid.append([])
        for j in range(r):
            node: Node = Node(i, j, gap, r)
            grid[i].append(node)
            
    return grid
            
def draw_grid(screen: pygame.Surface, r: int, w: int) -> None:
    gap: int = w // r
    
    for i in range(r):
        pygame.draw.line(screen, settings.BLACK, (0, i * gap), (settings.SIM_WIDTH, i * gap))
    for j in range(r + 1):
        pygame.draw.line(screen, settings.BLACK, (j * gap, 0), (j * gap, settings.SIM_WIDTH))
        
def draw(screen: pygame.Surface, grid: list[list[Node]], r: int, w: int) -> None:
    screen.fill(settings.WHITE)
    
    for row in grid:
        for node in row:
            node.draw(screen)
            
    draw_grid(screen, r, w)
    
    screen.blit(settings.RESET_TEXT, (settings.SIM_WIDTH + 20, settings.HEIGHT - settings.RESET_TEXT.get_height()))
    screen.blit(settings.START_TEXT, (settings.SIM_WIDTH + 20, settings.HEIGHT - 2 * settings.START_TEXT.get_height()))
    
    
    move_count_text = settings.H1_FONT.render(f"Move count : {settings.MOVE_COUNT}", True, settings.BLACK)
    move_length_text = settings.H2_FONT.render(f"Total lenght : {round(settings.MOVE_LENGTH, 2)}", True, settings.BLACK)
    screen.blit(move_count_text, (settings.SIM_WIDTH + 20, 0))
    screen.blit(move_length_text, (settings.SIM_WIDTH + 20, 45))
    
    pygame.display.update()
    
def get_clicked(pos: tuple[int, int], r: int, w: int) -> tuple[int, int]:
    gap: int = w // r
    
    x, y = pos
    
    row: int = x // gap
    col: int = y // gap
    
    return row, col

def reset_all_grid(grid: list[list[Node]]) -> None:
    for row in grid:
        for node in row:
            node.set_state(NodeState.WALKABLE)
            
def reset_grig(grid: list[list[Node]]) -> None:
    for row in grid:
        for node in row:
            if not node.state in (NodeState.START, NodeState.END, NodeState.BOUND):
                node.set_state(NodeState.WALKABLE)

def main(screen: pygame.Surface, w: int) -> None:    
    rows: int = settings.ROWS
    
    grid: list[list[Node]] = create_grid(rows, w)
    
    start: Node = None
    end: Node = None
    
    started: bool = False
    while True:        
        draw(screen, grid, rows, w)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start = None
                    end = None
                    reset_all_grid(grid)
                
            if not started:
                if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] < settings.SIM_WIDTH and pygame.mouse.get_pos()[1] < settings.HEIGHT:
                    r, c = get_clicked(pygame.mouse.get_pos(), rows, w)
                    node: Node = grid[r][c]
                    if not start:
                        start = node
                        start.set_state(NodeState.START)
                    elif not end:
                        end = node
                        end.set_state(NodeState.END)
                    elif not start == node and not end == node:
                        node.set_state(NodeState.BOUND)
                elif pygame.mouse.get_pressed()[2]:
                    r, c = get_clicked(pygame.mouse.get_pos(), rows, w)
                    node: Node = grid[r][c]
                    node.reset()
                    
                    if node == start:
                        start = None
                    if node == end:
                        end = None
                        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    reset_grig(grid)
                    if start and end:
                        for row in grid:
                            for node in row:
                                node.update_neighbors(grid)
                            
                        settings.MOVE_COUNT = 0
                        settings.MOVE_LENGTH = 0
                        
                        settings.MOVE_COUNT, settings.MOVE_LENGTH = astar_algorithm(lambda: draw(screen, grid, rows, w), grid, start, end)
                    
if __name__ == "__main__":
    main(screen, settings.SIM_WIDTH)