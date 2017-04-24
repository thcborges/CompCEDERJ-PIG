from tkinter import *
from BullsAndCowsGame.BullsAndCowsGame import BullsAndCowsGame
from BullsAndCowsGame.WordList import WordList
from BullsAndCowsGame.Status import Status


PLAYER1 = "Jogador 1"
PLAYER2 = "Jogador 2"


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.lbl_title = Label(self, text="Bulls and Cows Game")
        self.lbl_title.pack(side='top', expand=True, fill='x')

        self.pack()
        self.wlist = WordList("BullsAndCowsGame/palavras.txt")
        self.lbl_player = None
        self.lbl_bulls = None
        self.lbl_cows = None
        self.lbl_geese = None
        self.lbl_all_guessed_letters = None
        self.lbl_space = None
        self.entry_guess = None
        self.play = None
        self.opening = None
        self.condition = None
        self.btn_5_letters = None
        self. btn_4_letters = None
        self.btn_guess = None
        self.game = None
        self.bulls = StringVar()
        self.cows = StringVar()
        self.geese = StringVar()
        self.all_guessed_letters = StringVar()
        self.guess = StringVar()
        self.player = StringVar()
        
        self.open()

    def open(self):
        if self.condition == Status.OVER:
            self.play.destroy()
        self.opening = Frame(self.master)
        self.condition = Status

        self.btn_4_letters = Button(self.opening, text="4 LETRAS", command=self.four_letters)
        self.btn_5_letters = Button(self.opening, text="5 LETRAS", command=self.five_letters)

        for i in (self.lbl_title,
                  self.btn_4_letters,
                  self.btn_5_letters):
            i.pack(side='top')

        self.opening.pack()

    def four_letters(self):
        self.game = BullsAndCowsGame(self.wlist, 4)
        self.star_game()

    def five_letters(self):
        self.game = BullsAndCowsGame(self.wlist, 5)
        self.star_game()

    def star_game(self):
        self.condition = Status.START
        self.opening.destroy()
        self.runUI()
        self.player.set(PLAYER1)

    def runUI(self):
        self.game.startNewRound()
        print("PALAVRA SECRETA: {}".format(self.game.getSecretWord()))
        self.play = Frame(self.master)

        self.bulls.set(
            "Touros {}".format(self.spell(self.game.getBulls())))
        self.cows.set(
            "Vacas: {}".format(self.spell(self.game.getCows())))
        self.geese.set(
            "Gansos: {}".format(self.spell(self.game.getGeese())))
        self.all_guessed_letters.set(
            "Chutes: {}".format(self.spell(self.game.getAllGuessedLetters())))

        self.lbl_bulls = Label(
            self.play,
            textvar=self.bulls
        )
        self.lbl_cows = Label(
            self.play,
            textvar=self.cows
        )
        self.lbl_geese = Label(
            self.play,
            textvar=self.geese
        )
        self.lbl_all_guessed_letters = Label(
            self.play,
            textvar=self.all_guessed_letters
        )
        self.lbl_player = Label(
            self.play,
            textvar=self.player
        )

        for i in (self.lbl_bulls,
                  self.lbl_cows,
                  self.lbl_geese,
                  self.lbl_all_guessed_letters,
                  self.lbl_player):
            i.pack(side='top', expand=True, fill='x')
            i.configure(relief='ridge', border=2)

        self.lbl_space = Label(self.play,
                               text=" ",
                               height=1).pack(expand=False,
                                              side='top',
                                              fill='x')

        self.entry_guess = Entry(self.play, textvar=self.guess)
        self.entry_guess.bind("<Return>", self.attempt)
        self.entry_guess.pack(expand=False, side='top')
        self.entry_guess.focus_set()

        self.btn_guess = Button(self.play,
                                text="Chute",
                                command=self.attempt)
        self.btn_guess.pack(side='top',
                            expand=True,
                            fill='both')

        self.play.pack(fill='x')

    def attempt(self, x=None):
        print(self.guess.get())
        self.condition = self.game.guess(self.guess.get())
        print(self.condition)
        self.bulls.set(
            "Touros {}".format(self.spell(self.game.getBulls())))
        self.cows.set(
            "Vacas: {}".format(self.spell(self.game.getCows())))
        self.geese.set(
            "Gansos: {}".format(self.spell(self.game.getGeese())))
        self.all_guessed_letters.set(
            "Chutes: {}".format(self.spell(self.game.getAllGuessedLetters())))
        self.guess.set("")
        self.entry_guess.focus_set()
        self.game_situation()

    def game_situation(self):
        if self.condition == Status.INVALID_WORD:
            self.change_player()
        elif self.condition == Status.LOSE_TURN:
            self.change_player()
        elif self.condition == Status.KEEP_TURN:
            pass
        elif self.condition == Status.WIN:
            player = self.player.get()
            self.player.set("{} VENCEU!!! Parabéns!!".format(player))
            self.btn_guess.destroy()
            self.entry_guess.destroy()
            Button(self.play, text="Novo Jogo", command=self.open).pack()
            Button(self.play, text="Sair", command=self.quit).pack()
            self.condition = Status.OVER
        elif self.condition == Status.OVER:
            self.play.destroy()
            self.open()

    def change_player(self):
        if self.player.get() == PLAYER1:
            self.player.set(PLAYER2)
        else:
            self.player.set(PLAYER1)

    @staticmethod
    def spell(word):
        arrange = []
        for letter in word:
            arrange.append(letter)
        return " ".join(arrange)


wlist = WordList("BullsAndCowsGame/palavras.txt")
app = Application()
app.master.title("Bulls and Cows Game")
app.master.geometry("200x200")
mainloop()
