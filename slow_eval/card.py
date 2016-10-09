from tools import encode


class Card:
    STR_RANKS = 'AKQJT98765432'
    STR_SUITS = 'hdsc'

    def __init__(self, str_card):
        self.rank = str_card[0]
        self.suit = str_card[1]

    def __repr__(self):
        return "[%s%s]" % (self.rank, self.suit)

    def __str__(self):
        return self.__repr__()

    def get_bin(self):
        return encode(self.rank + self.suit)

