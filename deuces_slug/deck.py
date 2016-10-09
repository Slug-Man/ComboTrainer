from random import shuffle
from card import Card

class Deck:
    """
    Class representing a deck. The first time we create, we seed the static 
    deck with the list of unique card integers. Each object instantiated simply
    makes a copy of this object and shuffles it. 
    """
    _FULL_DECK = []

    def __init__(self):
        self.shuffle()

    def shuffle(self):
        # and then shuffle
        self.cards = Deck.GetFullDeck()
        shuffle(self.cards)

    def draw(self, n=1):
        if n == 1:
            return self.cards.pop(0)

        cards = []
        for i in range(n):
            cards.append(self.draw())
        return cards

    def draw_card(self, card):
        if isinstance(card, basestring):
            card = Card.new(card)
        try:
            self.cards.remove(card)
            return card
        except ValueError:
            raise ValueError("Deck.draw_card: card '%s' not in deck" % Card.int_to_str(card))

    def draw_rank(self, rank_char):
        rank_int = Card.CHAR_RANK_TO_INT_RANK[rank_char]

        for i, card in enumerate(self.cards):
            if Card.get_rank_int(card) == rank_int:
                return self.cards.pop(i)

        raise ValueError("Deck.draw_rank: no '%c' rank left in deck" % rank_char)

    def draw_suit(self, suit_char):
        suit_int = Card.CHAR_SUIT_TO_INT_SUIT[suit_char]

        for i, card in enumerate(self.cards):
            if Card.get_suit_int(card) == suit_int:
                return self.cards.pop(i)

        raise ValueError("Deck.draw_suit: no '%c' suit left in deck" % suit_char)

    def __str__(self):
        return Card.print_pretty_cards(self.cards)

    @staticmethod
    def GetFullDeck():
        if Deck._FULL_DECK:
            return list(Deck._FULL_DECK)

        # create the standard 52 card deck
        for rank in Card.STR_RANKS:
            for suit,val in Card.CHAR_SUIT_TO_INT_SUIT.iteritems():
                Deck._FULL_DECK.append(Card.new(rank + suit))

        return list(Deck._FULL_DECK)