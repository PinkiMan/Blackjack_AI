import random


class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

        self.rank = 0
        self.__calc_rank()


    def __calc_rank(self):
        if self.number.isnumeric():
            self.rank = [int(self.number)]

        elif self.number == "A":
            self.rank = [1, 11]
        elif self.number == "J":
            self.rank = [10]
        elif self.number == "Q":
            self.rank = [10]
        elif self.number == "K":
            self.rank = [10]




class Deck:
    def __init__(self):
        self.cards = []

        self.__fill_deck()


    def __fill_deck(self):
        for color in ["spades", "clubs", "diamonds", "hearts"]:
            for number in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(Card(color=color, number=number))

    def __str__(self):
        ret_string = ''
        card_num = 0
        for card in self.cards:
            if card_num % 13 == 0:
                ret_string += '\n'
            ret_string += card.color[0].upper()+card.number+'-'+str(card.rank)+'\t'
            card_num += 1
        return ret_string

    def shuffle(self):
        for _ in range(len(self.cards)**2):
            new_index = random.randint(0, len(self.cards)-1)

            new_deck = self.cards

            new_item = new_deck.pop(new_index)

            new_deck.append(new_item)

            self.cards = new_deck


    def take_card(self):
        if len(self.cards) > 0:
            card = self.cards.pop(0)
        else:
            card = None

        return card



