from constants import SHORT_MAP, CHAR_RANKS, CHAR_SUITS


class Card:

    @staticmethod
    def new(string):
        return SHORT_MAP[string]

    @staticmethod
    def get_str(card_int):
        return Card.get_rank(card_int) + Card.get_suit(card_int)

    @staticmethod
    def get_suit(card_int):
        return CHAR_SUITS[card_int % 4]

    @staticmethod
    def get_rank(card_int):
        return CHAR_RANKS[12 - (card_int >> 2)]


if __name__ == '__main__':
    ah = Card.new('Ah')
    print ah
    print "{0:b}".format(ah)
    print Card.get_suit(ah)

    print "{0:b}".format((13 << 2)+0)
    print "{0:b}".format((13 >> 2))
