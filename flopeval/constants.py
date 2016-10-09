CHAR_RANKS = 'AKQJT98765432'
CHAR_SUITS = 'hdsc'

SHORT_MAP = {}

for i, suit in enumerate(CHAR_SUITS):
    for j, rank in enumerate(CHAR_RANKS):
        SHORT_MAP[rank+suit] = (12-j << 2) + i

HANDS = [
    'Straight Flush',
    'Quads: Pocket Pair, Board Pair',
    'Quads: Board Trips',
    'Full House: Set, Board Pair',
    'Full House: Two Different Pocket Cards, Board Pair',
    'Full House: Pocket Pair, Board Trips',
    'Flush: Nut',
    'Flush',
    'Straight',
    'Trips: Set',
    'Trips: Board Pair',
    'Trips: Board Trips',
    'Two Pair: Two Different Pocket Cards',
    'Two Pair: Over Pocket Pair, Board Pair',
    'Two Pair: 2nd Pocket Pair, Board Pair',
    'Two Pair: Under Pocket Pair, Board Pair',
    'Two Pair: Pocket Card, Board Pair',
    'Pair: Over Pocket Pair',
    'Pair: Top Pair',
    'Pair: 2nd Pocket Pair',
    'Pair: 2nd Pair',
    'Pair: 3rd Pocket Pair',
    'Pair: 3rd Pair',
    'Pair: Under Pocket Pair',
    'Pair: Two Overcards with Ace, Pair on Board',
    'Pair: Pair on Board',
    'High Card: Two Overcards with Ace',
    'High Card'
]

HANDS_VALUE = {}

for i, h in enumerate(HANDS):
    HANDS_VALUE[h] = i

if __name__ == '__main__':
    for s, i in SHORT_MAP.iteritems():
        print s, "{0:b}".format(i)
