from constants import SHORT_MAP


class Deck:

    _CARDS = SHORT_MAP.values()
    _CARDS.sort(reverse=True)

    def __init__(self, remove=None):
        self.cards = list(Deck._CARDS)
        if remove is not None:
            self.remove(remove)

    def remove(self, card_list):
        for c in card_list:
            self.cards.remove(c)

if __name__ == '__main__':
    print Deck._CARDS