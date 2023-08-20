from enum import Enum
import settings

class NodeState(Enum):
    CLOSED = settings.RED
    OPEN = settings.GREEN
    BOUND = settings.BLACK
    WALKABLE = settings.WHITE
    START = settings.PURPLE
    END = settings.ORANGE
    PATH = settings.BLUE
    CAME_FROM = settings.GREY
    