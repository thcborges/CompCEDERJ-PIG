#!/usr/bin/env python
# codding: UTF-8
#
## @package BullsAndCowsGame
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
#
#  This module has the class that controls the game.
#


from Status import Status


##
#  Character to use as a placeholder for the hidden
#  characteres when displaying the "bulls"
PLACEHOLDER = "*"


## BullsAndCowsGame Class
#
#    Game controls for Bulls and Cows Game.
#
## @var self.__secret_word stores the word drawn.
#
## @var self.__secret_word_letters set that stores the letters of the secret word.
#
## @var self.__guessed list of letters that were attempt in the game.
#
## @var self.__guessed_letters set that stores the letters that have already been attempt.
#
## @var self.__bulls list with PLACEHOLDERS that are replaced every time a player hits a letter in its exact location.
#
## @var self.__geese list with the letters that were wrong every turn.
#
## @var self.__geese_leters set with all letters that were wrong in turn.
#
## @var self.__cows list with the letters that were already agreed, but was not in his right position.
#
class BullsAndCowsGame(object):

    ## Constructor method of the BullsAndCowsGame class.
    #
    #   Responsible for preparing the game.
    #   Leave the required variables blank so they are started.
    #
    def __init__(self, wlist, arg):
        self.wlist = wlist
        if isinstance(arg, int):
            self.__secret_word = self.wlist.generate(arg)

        if isinstance(arg, str):
            if self.wlist.check(arg.lower()):
                self.__secret_word = arg

        self.__secret_word_letters = set()
        self.__guessed = []
        self.__guessed_letters = set()
        self.__bulls = []
        self.__geese = []
        self.__geese_letters = set()
        self.__cows = []

    ##  Method startNewRound
    #
    #   prepares the game to start populating the variables:
    #   - self.__bulls with PLACEHOLDERS
    #   - self.__secret_word_letters with the letters of the word
    #
    def startNewRound(self):
        for i in range(len(self.__secret_word)):
            self.__bulls.append(PLACEHOLDER)
            self.__secret_word_letters.add(self.__secret_word[i])

    ## Method isOver.
    #
    #   Responsible for checking every round if the game is over.
    #
    def isOver(self):
        bulls = "".join(self.__bulls)
        if bulls == self.__secret_word:
            return True
        else:
            return False

    ## Method getSecretWord
    #
    #   Returns self.__secret_word.
    #   Used only for game testing.
    #
    def getSecretWord(self):
        return self.__secret_word

    ## Method getAllGuessedLetters
    #
    #   Returns self.__guessed as string.
    #
    def getAllGuessedLetters(self):
        return "".join(self.__guessed)

    ## Method getBulls
    #
    #   Returns self.__bulls as string.
    #
    def getBulls(self):
        return "".join(self.__bulls)

    ## Method getSecretWord
    #
    #   Returns self.__geese as string.
    #
    def getGeese(self):
        return "".join(self.__geese)

    ## Method getSecretWord
    #
    #   Returns self.__cows as string.
    #
    def getCows(self):
        return "".join(self.__cows)

    ## Method guess
    #
    #   Responsible for controlling the game.
    #   Processes a player's attempt and returns the appropriate state.
    #
    def guess(self, word):
        old_bulls = self.__bulls[:]
        word = word.lower()
        self.__geese = []
        self.__geese_letters = set()
        status = Status
        if self.wlist.check(word) and len(word) == len(self.__secret_word):
            for w in range(len(word)):
                if word[w] not in self.__guessed_letters:
                    self.__guessed_letters.add(word[w])
                    self.__guessed += word[w]

                if word[w] == self.__secret_word[w]:
                    self.__bulls[w] = word[w]

                elif word[w] in self.__secret_word_letters:
                    self.__cows += word[w]
                    self.__secret_word_letters.discard(word[w])

                elif word[w] not in self.__geese_letters:
                    self.__geese_letters.add(word[w])
                    self.__geese += word[w]

        else:
            return status.INVALID_WORD

        if old_bulls == self.__bulls:
            return status.LOSE_TURN
        elif self.isOver():
            return status.WIN
        else:
            return status.KEEP_TURN
