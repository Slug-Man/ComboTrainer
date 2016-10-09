from tools import STR_RANKS, STR_SUITS

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

if __name__ == '__main__':
    print "{0:b}".format(encode('2c'))
