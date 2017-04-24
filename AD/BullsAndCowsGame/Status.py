from enum import Enum


class Status(Enum):
    START = 0
    INVALID_WORD = 1
    LOSE_TURN = 2
    KEEP_TURN = 3
    WIN = 4
    OVER = 5
