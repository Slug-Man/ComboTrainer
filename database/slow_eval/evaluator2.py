from tools import STR_RANKS


class FlopEvaluator2:

    LUT = None

    def __init__(self, board, hand):
        self.board = board
        self.hand = hand

    def get_made(self):
        if self.LUT is not None:
            try:
                return self.LUT[u'%d' % self.board.get_bin() + self.hand.get_bin()]
            except KeyError:
                pass

        self._calc_flush_or_straight()

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