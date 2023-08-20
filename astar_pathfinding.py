import pygame
import math

from node import Node
from node_state_enum import NodeState
from queue import PriorityQueue

def h(node1: tuple, node2: tuple) -> float:
    x1, y1 = node1
    x2, y2 = node2
    
    return abs(x2 - x1) + abs(y2 - y1)

def d(node1: tuple, node2: tuple) -> float:
    x1, y1 = node1
    x2, y2 = node2
    
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def reconstruct_path(came_from: dict, current: Node, draw) -> tuple[int, int]:
    i = 0
    l = 0
    last: Node = current
    while current in came_from:
        current = came_from[current]
        l += d(last.get_pos(), current.get_pos())
        current.set_state(NodeState.PATH)
        last = current
        draw()
        i += 1
    return i, l
    

def astar_algorithm(draw, grid: list[list[Node]], start: Node, end: Node) -> tuple[int, int]:
    count: int = 0
    length: int = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    
    came_from: dict = {}
    
    g_score: dict = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    
    f_score: dict = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
    
    open_set_hash: set = {start}
    
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                    
        current: Node = open_set.get()[2]
        open_set_hash.remove(current)
        
        if current == end:
            count, length = reconstruct_path(came_from, end, draw)
            start.set_state(NodeState.START)
            end.set_state(NodeState.END)
            return count, length
        
        for neighbor in current.neighbors:
            tentative_g_score = g_score[current] + d(current.get_pos(), neighbor.get_pos())
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor.get_pos(), end.get_pos())
                
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    
                    neighbor.set_state(NodeState.OPEN)
        draw()
        
        if current != start:
            current.set_state(NodeState.CLOSED)
            
    return count, length