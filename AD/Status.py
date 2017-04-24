from enum import Enum


##
#  Enumerated type representing possible status after
#  guessing a word in the BullsAndCows game.
#
class Status(Enum):
    START = 0
    INVALID_WORD = 1
    LOSE_TURN = 2
    KEEP_TURN = 3
    WIN = 4
    OVER = 5
