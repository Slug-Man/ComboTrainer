import numpy

from constants import HANDS_VALUE


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


if __name__ == '__main__':
    from itertools import combinations
    from card import Card
    from deck import Deck
    import time
    from itertools import count

    #f1, f2, f3 = Card.new('Th'), Card.new('8h'), Card.new('9d')
    t = time.time()
    counter = count()
    for f1, f2, f3 in combinations(Deck().cards, 3):
        for c1, c2 in combinations(Deck(remove=[f1, f2, f3]).cards, 2):
            result = FlopEvaluator.evaluate([f1, f2, f3], [c1, c2])
            #print FlopEvaluator.evaluate([f1, f2, f3], [c1, c2]),
            #print "[%s %s]" % (Card.get_str(c1), Card.get_str(c2))
            #counter.next()
        #   print "%s%s%s" % (Card.get_str(f1), Card.get_str(f2), Card.get_str(f3)), time.time()-t

    print time.time()-t