from tools import STR_RANKS


class CardSet:
    STR_SUITS = 'hdsc'

    sorted_by_rank = False

    BIN_CACHE = None

    def __init__(self, card_list=None):
        if card_list is None:
            self.card_list = []
        else:
            self.card_list = card_list
        self.get_bin()

    def sort_by_rank(self):
        if self.sorted_by_rank:
            return

        for i in range(1, len(self.card_list)):
            for j in range(0, i):
                if STR_RANKS[self.card_list[j].rank] < STR_RANKS[self.card_list[i].rank]:
                    swap_temp = self.card_list[i]
                    self.card_list[i] = self.card_list[j]
                    self.card_list[j] = swap_temp
        self.sorted_by_rank = True

    def get_bin(self):
        if self.BIN_CACHE is not None:
            return self.BIN_CACHE

        b = 0
        for c in self:
            b += c.get_bin()

        self.BIN_CACHE = b
        return b

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        string = ""
        for c in self.card_list:
            string += "%s " % c

        return "[%s]" % string[:-1]

    def __getitem__(self, item):
        return self.card_list[item]

    def __len__(self):
        return len(self.card_list)
