from itertools import product, combinations
import time
import json

from card import Card
from cardset import CardSet
from evaluator import FlopEvaluator
from tools import STR_RANKS, STR_SUITS


def write_table():
    table = {}
    t = time.time()
    for c1, c2, c3, c4, c5 in combinations(product(STR_RANKS.keys(), STR_SUITS),
                                           5):
        cset = CardSet([Card("".join(c1)),
                        Card("".join(c2)),
                        Card("".join(c3)),
                        Card("".join(c4)),
                        Card("".join(c5))])
        flop_eval = FlopEvaluator(cset)
        made = flop_eval.get_made()
        table[cset.get_bin()] = made.keys()[made.values().index(True)]
    with open('./lut/test.lut', 'w') as f:
        json.dump(table, f)
    print t, time.time(), time.time()-t


def read_table():
    with open('./lut/test.lut', 'r') as f:
        return json.load(f)

if __name__ == '__main__':
    c1 = Card('7c')
    c2 = Card('5c')
    c3 = Card('4c')
    c4 = Card('3c')
    c5 = Card('2s')

    cset = CardSet([c4, c2, c3, c1, c5])
    table = read_table()
    print table[u'%d' % cset.get_bin()]
