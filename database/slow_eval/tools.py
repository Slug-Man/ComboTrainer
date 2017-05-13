STR_RANKS = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
}
STR_SUITS = 'hdsc'

SUIT2BIN = {
    'h': 13*3,
    'd': 13*2,
    's': 13*1,
    'c': 13*0
}
RANK2BIN = {}

for k, v in STR_RANKS.iteritems():
    RANK2BIN[k] = 1 << v-1


def encode(string):
    return RANK2BIN[string[0]] << SUIT2BIN[string[1]]
