import numpy

from constants import HANDS_VALUE, HANDS
from itertools import combinations

from deck import Deck


class FlopEvaluator:

    @staticmethod
    def _split_rank_suit(cards):
        if not isinstance(cards, list):
            cards = [cards]

        ranks = []
        suits = []
        for c in cards:
            ranks.append(c >> 2)
            suits.append(c % 4)

        return ranks, suits

    @staticmethod
    def get_board_state(board):
        ranks, suits = FlopEvaluator._split_rank_suit(board)
        return max([ranks.count(ranks[0]), ranks.count(ranks[1]), 1])

    @staticmethod
    def get_hand_state(hand):
        ranks, suits = FlopEvaluator._split_rank_suit(hand)
        return max([ranks.count(ranks[0]), 1])

    @staticmethod
    def evaluate(board, hand):
        board_ranks, board_suits = FlopEvaluator._split_rank_suit(board)
        hand_ranks, hand_suits = FlopEvaluator._split_rank_suit(hand)
        ranks = board_ranks + hand_ranks
        suits = board_suits + hand_suits
        rank_count = numpy.bincount(numpy.array(ranks))

        if max(rank_count) == 1:
            if FlopEvaluator.is_flush(suits):
                if FlopEvaluator.is_straight(ranks):
                    return HANDS_VALUE['Straight Flush']
                else:
                    if (12 in hand_ranks) \
                            or (12 in board_ranks and 11 in hand_ranks) \
                            or (12 in board_ranks and 11 in board_ranks and 10 in hand_ranks) \
                            or (12 in board_ranks and 11 in board_ranks and 10 in board_ranks and 9 in hand_ranks):
                        return HANDS_VALUE['Flush: Nut']
                    else:
                        return HANDS_VALUE['Flush']
            elif FlopEvaluator.is_straight(ranks):
                return HANDS_VALUE['Straight']
            else:
                if 12 in hand_ranks and min(hand_ranks) > max(board_ranks):
                    return HANDS_VALUE['High Card: Two Overcards with Ace']
                else:
                    return HANDS_VALUE['High Card']

        elif max(rank_count) == 2:
            if 2 in numpy.bincount(rank_count):
                if hand_ranks[0] == hand_ranks[1]:
                    if hand_ranks[0] > max(board_ranks):
                        return HANDS_VALUE['Two Pair: Over Pocket Pair, Board Pair']
                    elif hand_ranks[0] > min(board_ranks):
                        return HANDS_VALUE['Two Pair: 2nd Pocket Pair, Board Pair']
                    else:
                        return HANDS_VALUE['Two Pair: Under Pocket Pair, Board Pair']
                elif 2 in numpy.bincount(numpy.array(board_ranks)):
                    return HANDS_VALUE['Two Pair: Pocket Card, Board Pair']
                else:
                    return HANDS_VALUE['Two Pair: Two Different Pocket Cards']
            else:
                if hand_ranks[0] == hand_ranks[1]:
                    board_ranks.sort(reverse=True)
                    if hand_ranks[0] > max(board_ranks):
                        return HANDS_VALUE['Pair: Over Pocket Pair']
                    elif hand_ranks[0] > max(board_ranks[1:]):
                        return HANDS_VALUE['Pair: 2nd Pocket Pair']
                    elif hand_ranks[0] > max(board_ranks[2:]):
                        return HANDS_VALUE['Pair: 3rd Pocket Pair']
                    else:
                        return HANDS_VALUE['Pair: Under Pocket Pair']
                elif 2 in numpy.bincount(numpy.array(board_ranks)):
                    if min(hand_ranks) > max(board_ranks):
                        return HANDS_VALUE['Pair: Two Overcards with Ace, Pair on Board']
                    else:
                        return HANDS_VALUE['Pair: Pair on Board']
                else:
                    if 12 in hand_ranks and min(hand_ranks) > max(board_ranks):
                        return HANDS_VALUE['Pair: Two Overcards with Ace, Pair on Board']
                    else:
                        return HANDS_VALUE['Pair: Pair on Board']

        elif max(rank_count) == 3:
            if 2 in rank_count:
                if hand_ranks[0] == hand_ranks[1]:
                    if 3 in numpy.bincount(numpy.array(board_ranks)):
                        return HANDS_VALUE['Full House: Pocket Pair, Board Trips']
                    else:
                        return HANDS_VALUE['Full House: Set, Board Pair']
                else:
                    return HANDS_VALUE['Full House: Two Different Pocket Cards, Board Pair']
            else:
                if hand_ranks[0] == hand_ranks[1]:
                    return HANDS_VALUE['Trips: Set']
                elif 2 in numpy.bincount(numpy.array(board_ranks)):
                    return HANDS_VALUE['Trips: Board Pair']
                else:
                    return HANDS_VALUE['Trips: Board Trips']

        elif max(rank_count) == 4:
            if hand_ranks[0] == hand_ranks[1]:
                return HANDS_VALUE['Quads: Pocket Pair, Board Pair']
            else:
                return HANDS_VALUE['Quads: Board Trips']

    @staticmethod
    def is_flush(suits):
        return suits.count(suits[0]) == 5

    @staticmethod
    def is_straight(ranks):
        ranks.sort()
        current = ranks[0]
        for r in ranks[1:]:
            if current == r - 1:
                current = r
            else:
                return False
        return True

    @staticmethod
    def evaluate_for_range(board, pocket_combos=None):
        """
        Computes total number of combos of each hand strength for a given range and community board.
        
        WARNING! board and pocket_combos must not share any common card ints.
        
        :param board: list of three card ints representing the flop.
        :param pocket_combos: list of lists of two card ints (see hand_range_to_cards() in rangeparser.py). Defaults to
            whole deck.
        :return: dict where hand strength (represented by an int -- see constants.py) is mapped to number of combos.
        """
        # TODO: some way handle card int duplicates in board and pocket_combos

        if pocket_combos is None:
            pocket_combos = combinations(Deck(remove=board).cards, 2)

        results_dict = {}

        for c1, c2 in pocket_combos:
            temp_result = FlopEvaluator.evaluate(board, [c1, c2])
            try:
                results_dict[temp_result] += 1
            except KeyError:
                results_dict[temp_result] = 1

        return results_dict


def prettify_eval_results(results):
    pretty_results = {}
    for k, v in results.iteritems():
        # TODO int() is a hack for distinctflops.py pls remove
        pretty_results[HANDS[int(k)]] = v
    return pretty_results

if __name__ == '__main__':
    from card import Card
    from constants import HANDS
    import time
    from itertools import count
    from rangeparser import hand_range_to_cards, card_ints_to_str

    flop = [Card.new('As'), Card.new('Ac'), Card.new('Ad')]

    aaa = FlopEvaluator.evaluate_for_range(flop)
    print 'flop: AsAcAd range: random'
    for v in aaa:
        print HANDS[v], '-', aaa[v]

    ttp = FlopEvaluator.evaluate_for_range(flop, hand_range_to_cards('22+,A2s+,A2o+', flop))
    print 'flop: AsAcAd range: 22+,A2s+,A2o+'
    for v in ttp:
        print HANDS[v], '-', ttp[v]