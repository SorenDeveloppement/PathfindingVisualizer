import pygame
pygame.font.init()

WIDTH: int = 1200
SIM_WIDTH: int = 800
HEIGHT: int = 800

FPS: int = 60

ROWS: int = SIM_WIDTH // 25

# Colors
RED: tuple[int] = (255, 0, 0)
GREEN: tuple[int] = (0, 255, 0)
BLUE: tuple[int] = (0, 0, 255)
YELLOW: tuple[int] = (255, 255, 0)
WHITE: tuple[int] = (255, 255, 255)
BLACK: tuple[int] = (0, 0, 0)
PURPLE: tuple[int] = (128, 0, 128)
ORANGE: tuple[int] = (255, 156, 0)
GREY: tuple[int] = (128, 128, 128)
TRUQUOISE: tuple[int] = (64, 224, 208)

MOVE_COUNT: int = 0
MOVE_LENGTH: float = 0

# Texts
TEXT_FONT: pygame.font.Font = pygame.font.SysFont("Arial", 20)
H1_FONT: pygame.font.Font = pygame.font.SysFont("Arial", 40)
H2_FONT: pygame.font.Font = pygame.font.SysFont("Arial", 30)

RESET_TEXT = TEXT_FONT.render("R: Reset grid", True, BLACK)
START_TEXT = TEXT_FONT.render("Space: Start pathfinding", True, BLACK)