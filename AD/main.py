import os
import sys

import BullsAndCowsGame
from TextUI import TextUI
from WordList import WordList


##########################################
##
##  Strings constants present in the game
##
##  Alphabetical order in the constants name
##
##########################################
BULLS_AND_COWS = "||########################||\n" \
                 "||    BULLS AND COWS      ||\n" \
                 "||         GAME           ||\n" \
                 "||########################||\n"
DICTIONARY = "palavras.txt"
DIFICULTY = "Escolha a dificuldade do jogo.\n"
ERROR = "ERRO!"
LETTERS_NUMBER = "  Digite '4' para palavras com QUATRO letras\n  Digite '5' para palavras com CINCO letras\n    => "


## Function check_size
#   Responsible for checking the difficulty of the game by
#   informing the size of the word to be guessed.
#
def check_size():
    os.system("cls" if os.name == "nt" else "clear")
    print(BULLS_AND_COWS)
    word_size = input(DIFICULTY + LETTERS_NUMBER)
    if word_size == "4" or word_size == "5":
        return int(word_size)
    else:
        print(ERROR)
        return check_size()

## Function main
#
#   Function where each turn of the game happens.
#
def main(argv=None):
    if argv is None:
        argv = sys.argv

    play = True
    while play:
        wlist = WordList(DICTIONARY)
        size = check_size()

        game = BullsAndCowsGame(wlist, size)
        ui = TextUI(game)
        ui.runUI()
        play = ui.playAgain()


if __name__ == '__main__':
    sys.exit(main())
