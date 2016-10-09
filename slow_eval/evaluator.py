import json

from cardset import CardSet
from tools import STR_RANKS


class FlopEvaluator:

    STFL = None  # straight flush
    FL = None  # flush
    ST = None  # straight

    QUADS = None
    FH = None
    TRIPS = None
    TWOPAIR = None
    PAIR = None
    HIGH = None

    LUT = None

    def __init__(self, card_set=None):
        if card_set is None:
            self.card_set = CardSet()
        else:
            self.card_set = card_set

    def use_table(self, table):
        self.LUT = table

    def get_made(self):
        if self.LUT is not None:
            try:
                return self.LUT[u'%d' % self.card_set.get_bin()]
            except KeyError:
                pass

        self._calc_flush_or_straight()
        self._calc_multiples()

        made = {
            "Straight Flush": self.STFL,
            "Flush": self.FL,
            "Straight": self.ST,
            "Quads": self.QUADS,
            "Full House": self.FH,
            "Trips": self.TRIPS,
            "Two Pair": self.TWOPAIR,
            "Pair": self.PAIR,
            "High Card": self.HIGH,
        }
        return made.keys()[made.values().index(True)]

    def _calc_flush_or_straight(self):
        if self.STFL is not None:
            return
        if len(self.card_set) != 5:
            return

        self.card_set.sort_by_rank()

        straight_cur = STR_RANKS[self.card_set[0].rank]
        first_suit = self.card_set[0].suit
        for c in self.card_set[1:]:
            if self.ST is None and straight_cur == STR_RANKS[c.rank]+1:
                straight_cur = STR_RANKS[c.rank]
            else:
                self.ST = False
            if c.suit != first_suit:
                self.FL = False

        if self.ST is None:
            self.ST = True
        if self.FL is None:
            self.FL = True
        if self.ST and self.FL:
            self.STFL = True
            self.ST = False
            self.FL = False
        else:
            self.STFL = False

    def _calc_multiples(self):
        if any((self.STFL, self.FL, self.ST)):
            self.QUADS = False
            self.FH = False
            self.TRIPS = False
            self.TWOPAIR = False
            self.PAIR = False
            self.HIGH = False
            return
        elif self.QUADS is not None:
            return

        ranks = self._rank_count()

        self.QUADS = ranks.values().count(4) == 1
        self.TRIPS = ranks.values().count(3) == 1
        self.TWOPAIR = ranks.values().count(2) == 2
        self.PAIR = ranks.values().count(2) == 1
        self.HIGH = ranks.values().count(1) == 5

        if self.TRIPS and self.PAIR:
            self.FH = True
            self.TRIPS = False
            self.PAIR = False
        else:
            self.FH = False

    def _rank_count(self):
        ranks = {}
        for c in self.card_set:
            if c.rank in ranks:
                ranks[c.rank] += 1
            else:
                ranks[c.rank] = 1
        return ranks