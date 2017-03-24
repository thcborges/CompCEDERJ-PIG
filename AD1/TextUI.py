#!/usr/bin/env python
# codding: UTF-8
#
## @package BullsAndCowsGame
#
#  Bulls and Cows game (also known as Cows and Bulls or Pig and Bulls or Bulls and Cleots)
#  is an old code-breaking paper and pencil game for two players,
#  predating the similar commercially marked board game Mastermind.
#
#  @author Thiago da Cunha Borges under the guidance of Paulo Roma
#  @since 11/03/2017
#  @see http://en.wikipedia.org/wiki/Bulls_and_cows
#  @see http://www.python-course.eu/sets_frozensets.php
#  @see https://www.dicio.com.br/palavras-com-cinco-letras/
#

import sys
import os
import BullsAndCowsGame
from WordList import WordList
from Status import Status
from random import randint

##########################################
##
##  Strings constants present in the game
##
##  Alphabetical order in the constants name
##
##########################################
ATTEMPT = "Tente uma palavra: "
BULLS = "  - Bulls: "
BULLS_AND_COWS = "||########################||\n" \
                 "||    BULLS AND COWS      ||\n" \
                 "||         GAME           ||\n" \
                 "||########################||\n"
COWS = "  - Cows: "
DICTIONARY = "palavras.txt"
DIFICULTY = "Escolha a dificuldade do jogo.\n"
ERROR = "ERRO!"
GEESE = "  - Gansos: "
GUESS = "  - Chutes: "
INVALID_WORD = "Essa palavra não existe em nosso dicionário.\n\n  - PRÓXIMO JOGADOR"
KEEP_TURN = "Muito bem!\n\n Continue jogando"
LETTERS_NUMBER = "  Digite '4' para palavras com QUATRO letras\n  Digite '5' para palavras com CINCO letras\n    => "
LOSE_TURN = "Nenhum touro no chute.\n\n  - PRÓXIMO JOGADOR"
NEW_GAME = "Novo jogo"
OVER = "o jogo acabou"
PLAYER1 = "Jogador 1"
PLAYER2 = "Jogador 2"
PLAY_AGAIN = "Deseja Jogar novamente? (S/N)\n"
WIN = "PARABÉNS!!!\n{0}\nVENCEU O JOGO!"

## TexUI class
#
#   Responsible for the user interface of the game.
#
#   @var self.player saves the current player.
#
#   @var self.__game saves the game running.
#
#   @var self.status used to check the current situation of the game.
#
#   @var self.condition saves the current state of the game.
# It is started as self.status.START informing you that a new game was created
#
class TextUI:
    ## Contingent class.
    #
    #  Starts the necessary variables.
    #
    def __init__(self, given_game):
        self.player = PLAYER1
        self.__game = given_game
        self.status = Status
        self.condition = self.status.START

    ## Method runUI
    #
    #   Where the game happens.
    #   The state of the game is tested at each tie so that it is possible
    #   to know what happens next, how to keep exchanging or keeping the player.
    #   The game loop runs until there is a winner, which is shown on the screen.
    #
    def runUI(self):
        self.__game.startNewRound()
        status = Status
        self.condition = status.START
        # lista = WordList("palavras.txt")  ##  Remove comment to automate the game
        while self.condition != status.OVER:
            self.display()
            print(self.player)
            self.condition = self.__game.guess(input(ATTEMPT))
            #  To automate the game you can comment the above line and remove the comment from the next lines.
            # n = randint(0, 499)
            # print("Attempt: ", lista.list4[n])                    ## => Remove only to choose 4-letter words during the game.
            # self.condition = self.__game.guess(lista.list4[n])    ## => Remove only to choose 4-letter words during the game.
            # print("Attempt: ", lista.list5[n])                    ## => Remove only to choose 5-letter words during the game.
            # self.condition = self.__game.guess(lista.list5[n])    ## => Remove only to choose 5-letter words during the game.
            if self.condition == status.WIN:
                self.display()
                self.condition = status.OVER

            elif self.condition == status.LOSE_TURN or self.condition == status.INVALID_WORD:
                self.change_player()

    ## Method change_player
    #
    #  Responsible for changing the player of the time
    #
    def change_player(self):
        self.player = PLAYER2 if self.player == PLAYER1 else PLAYER1

    ## Static method spell
    #
    #   Responsible for the presentation of the letters in the game.
    #   A space is placed between them so that the presentation and the aspect of the game is more pleasant
    #
    @staticmethod
    def spell(word):
        list = []
        for letter in word:
            list.append(letter)
        return " ".join(list)

    ## Method display
    #
    #   Responsible for the presentation of the game on the screen.
    #   It clears the screen every time it is called and assembles
    #   the screen always as specified through the game state.
    #
    def display(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(BULLS_AND_COWS)
        print(BULLS, self.spell(self.__game.getBulls()))
        print(COWS, self.spell(self.__game.getCows()))
        print(GEESE, self.spell(self.__game.getGeese()))
        print(GUESS, self.spell(self.__game.getAllGuessedLetters()))
        print("\n" + self.condition_message() + "\n")

    ## Method condition_message
    #
    #   Returns a message according to the condition of the game.
    #   This message is displayed on the screen using the display method
    #
    def condition_message(self):
        if self.condition == self.status.START:
            return NEW_GAME
        elif self.condition == self.status.INVALID_WORD:
            return INVALID_WORD
        elif self.condition == self.status.LOSE_TURN:
            return LOSE_TURN
        elif self.condition == self.status.KEEP_TURN:
            return KEEP_TURN
        elif self.condition == self.status.WIN:
            return WIN.format(self.player)
        else:
            return ERROR

    ## Method playAgain
    #
    # Asks the players if they want to start a new game turn
    #
    def playAgain(self):
        play = input(PLAY_AGAIN).upper()
        if play == "S" or play == "Y":
            os.system("cls" if os.name == "nt" else "clear")
            return True
        elif play == "N":
            os.system("cls" if os.name == "nt" else "clear")
            return False
        else:
            return self.playAgain()
