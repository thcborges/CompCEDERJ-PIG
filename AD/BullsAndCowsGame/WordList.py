from random import randint

FOUR = 4
FIVE = 5


class WordList:

    def __init__(self, filename):
        try:
            with open(filename, "r", encoding='UTF-8') as file:
                words_list = file.read()
                data = words_list.split("\n")
                self.list4, self.list5 = self.lists_generate(data)
        except Exception as e:
            print("ERROR!! " + str(e))
            exit(1)

    @staticmethod
    def lists_generate(list):
        list_four, list_five = [], []
        for word in list:
            if len(word) == FOUR:
                list_four.append(word)
            elif len(word) == FIVE:
                list_five.append(word)

        return list_four, list_five

    def check(self, word):
        if len(word) != FOUR and len(word) != FIVE:
            return False

        elif len(word) == FOUR and self.binarySearch(self.list4, word) == -1:
            return False

        elif len(word) == FIVE and self.binarySearch(self.list5, word) == -1:
            return False

        else:
            return True

    def generate(self, size):
        if size != FOUR and size != FIVE:
            return None

        elif size == FOUR:
            num = randint(0, len(self.list4))
            return self.list4[num]

        elif size == FIVE:
            num = randint(0, len(self.list5))
            return self.list5[num]

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
