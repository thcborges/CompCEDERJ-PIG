import os, sys

from BullsAndCowsGame.BullsAndCowsGame import BullsAndCowsGame
from BullsAndCowsGame.Status import Status
from BullsAndCowsGame.WordList import WordList

ATTEMPT = "Tente uma palavra: "
BULLS = "  - Bulls: "
BULLS_AND_COWS = "||########################||\n" \
                 "||    BULLS AND COWS      ||\n" \
                 "||         GAME           ||\n" \
                 "||########################||\n"
COWS = "  - Cows: "
DICTIONARY = "BullsAndCowsGame\palavras.txt"
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


class TextUI:

    def __init__(self, given_game):
        self.player = PLAYER1
        self.__game = given_game
        self.status = Status
        self.condition = self.status.START


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

    def change_player(self):
        self.player = PLAYER2 if self.player == PLAYER1 else PLAYER1

    @staticmethod
    def spell(word):
        list = []
        for letter in word:
            list.append(letter)
        return " ".join(list)

    def display(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(BULLS_AND_COWS)
        print(BULLS, self.spell(self.__game.getBulls()))
        print(COWS, self.spell(self.__game.getCows()))
        print(GEESE, self.spell(self.__game.getGeese()))
        print(GUESS, self.spell(self.__game.getAllGuessedLetters()))
        print("\n" + self.condition_message() + "\n==> Palavra secreta: " + self.__game.getSecretWord() + "\n")

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


def check_size():
    os.system("cls" if os.name == "nt" else "clear")
    print(BULLS_AND_COWS)
    word_size = input(DIFICULTY + LETTERS_NUMBER)
    if word_size == "4" or word_size == "5":
        return int(word_size)
    else:
        print(ERROR)
        return check_size()


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
