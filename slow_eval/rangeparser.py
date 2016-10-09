import itertools

from card import Card
from cardset import CardSet

ordered_ranks = '23456789TJQKA'
random_range = "22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,72s+,62s+,52s+,42s+," \
               "32s,A2o+,K2o+,Q2o+,J2o+,T2o+,92o+,82o+,72o+,62o+,52o+,42o+,32o"
suited = 'hcsd'


def hand_range_to_cards(ranges_str):
    if ranges_str == 'random':
        ranges_str = random_range

    ranges = ranges_str.split(',')

    combos = []
    for r in ranges:
        if '+' in r:
            for l in map(_comboify_hand, _split_pluses(r)):
                combos += l
        elif '-' in r:
            for l in map(_comboify_hand, _split_seq(r)):
                combos += l
        else:
            combos += _comboify_hand(r)

    hands = map(_combo_to_hand, combos)

    return hands


def _split_pluses(range_str):
    top = range_str[0]
    bottom = range_str[1]
    suit = range_str[2]

    indiv_ranges = []

    top_i = ordered_ranks.index(top)
    bottom_i = ordered_ranks.index(bottom)
    if bottom_i < top_i:
        for rank in ordered_ranks[bottom_i:top_i]:
            indiv_ranges.append("%c%c%c" % (top, rank, suit))
    elif bottom_i == top_i:
        for rank in ordered_ranks[bottom_i:]:
            indiv_ranges.append("%c%c" % (rank, rank))

    return indiv_ranges


def _split_seq(range_str):
    top, bottom = range_str.split('-')
    suit = range_str[2]

    indiv_ranges = []

    top_i = ordered_ranks.index(top[1])+1
    bottom_i = ordered_ranks.index(bottom[1])
    if top[0] == top[1] and bottom[0] == bottom[1]:
        for rank in ordered_ranks[bottom_i:top_i]:
            indiv_ranges.append("%c%c" % (rank, rank))
    elif bottom_i < top_i:
        for rank in ordered_ranks[bottom_i:top_i]:
            indiv_ranges.append("%c%c%c" % (top[0], rank, suit))

    return indiv_ranges


def _comboify_hand(hand):
    indiv_ranges = []

    if hand[-1] == 's':
        for suit in suited:
            indiv_ranges.append("%s%s%s%s" % (hand[0], suit, hand[1], suit))
    elif hand[-1] == 'o':
        for suit1, suit2 in itertools.permutations(suited, 2):
            indiv_ranges.append("%s%s%s%s" % (hand[0], suit1, hand[1], suit2))
    elif hand[0] == hand[1]:
        for suit1, suit2 in itertools.combinations(suited, 2):
            indiv_ranges.append("%s%s%s%s" % (hand[0], suit1, hand[1], suit2))

    return indiv_ranges


def _combo_to_hand(combo):
    return CardSet([Card(combo[:2]), Card(combo[2:])])

