from BullsAndCowsGame.Status import Status


PLACEHOLDER = "*"


class BullsAndCowsGame(object):

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

    def startNewRound(self):
        for i in range(len(self.__secret_word)):
            self.__bulls.append(PLACEHOLDER)
            self.__secret_word_letters.add(self.__secret_word[i])

    def isOver(self):
        bulls = "".join(self.__bulls)
        if bulls == self.__secret_word:
            return True
        else:
            return False

    def getSecretWord(self):
        return self.__secret_word

    def getAllGuessedLetters(self):
        return "".join(self.__guessed)

    def getBulls(self):
        return "".join(self.__bulls)

    def getGeese(self):
        return "".join(self.__geese)

    def getCows(self):
        return "".join(self.__cows)

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
