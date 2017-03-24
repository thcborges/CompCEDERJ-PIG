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
#  This module is responsable to create, manage and check the list of word to the game.
#
from random import randint
#  import requests

FOUR = 4
FIVE = 5


## Class WordList
#
#  This class is responsible for creating a list of words.
#  These words are taken from a file whose name is provided by the class constructor.
#  It is also responsible for checking if there is a certain word in this list,
#  Find a word on this list
#  And return a word if the size matches the size of the words in the list.
#
class WordList:

    ##WordList Constructor
    #  Constructs word lists from the file whose name is entered.
    #  Separate four-letter words in a list and five-letter words into another list,
    #  thus making the search for words more efficient in the static binarySearch method.
    #
    ## @var self.list4
    #   store a list of four letters words
    #
    ## @var self.list5
    #   store a list of five letters words
    #
    def __init__(self, filename):
        try:
            with open(filename, "r", encoding='UTF-8') as file:
                words_list = file.read()
                data = words_list.split("\n")
                self.list4, self.list5 = self.lists_generate(data)
        except Exception as e:
            print("ERROR!! " + str(e))
            # The implementation below would allow you to import a word file from a web location
            # but it does not work on some python installations. I tested it in Python 3.6 and it worked.
            # try:
            #     file = requests.get('http://www.saladeestudos.esy.es/palavras.txt')
            #     data = file.content.decode("utf-8").split("\n")
            #     self.list4, self.list5 = self.lists_generate(data)
            # except Exception as e:
            #     print("ERRO!! " + str(e))
            #     print("Não foi possível acessar o arquivo.")
            #     exit(1)
            exit(1)

    ##  Lists_generate
    #
    ## @param list list of words.
    #
    # Returns two lists, one with four letters and one with five letters.
    #
    @staticmethod
    def lists_generate(list):
        list_four, list_five = [], []
        for word in list:
            if len(word) == FOUR:
                list_four.append(word)
            elif len(word) == FIVE:
                list_five.append(word)

        return list_four, list_five

    ## Method check
    #
    #  method that checks if a received word is in the word list
    def check(self, word):
        if len(word) != FOUR and len(word) != FIVE:
            return False

        elif len(word) == FOUR and self.binarySearch(self.list4, word) == -1:
            return False

        elif len(word) == FIVE and self.binarySearch(self.list5, word) == -1:
            return False

        else:
            return True

    ## Method generate
    #
    #  Method that return a random word from the word list
    def generate(self, size):
        if size != FOUR and size != FIVE:
            return None

        elif size == FOUR:
            num = randint(0, len(self.list4))
            return self.list4[num]

        elif size == FIVE:
            num = randint(0, len(self.list5))
            return self.list5[num]


    ## Static method binary_search
    #
    #  Method that search and returns the position of the word in the list
    #  If the word is not in the list returns -1
    @staticmethod
    def binarySearch(alist, word):
        inf = 0
        sup = len(alist) - 1

        while inf <= sup:
            meio = (inf + sup) // 2
            if word == alist[meio]:
                return meio
            elif word < alist[meio]:
                sup = meio - 1
            else:
                inf = meio + 1

        return -1
