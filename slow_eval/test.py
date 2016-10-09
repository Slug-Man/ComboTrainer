import time
from itertools import product, combinations

import basic_lut
from card import Card
from cardset import CardSet
from evaluator import FlopEvaluator
from tools import STR_RANKS, STR_SUITS

c1 = Card('Ah')
c2 = Card('Kh')
c3 = Card('Qh')
c4 = Card('Jh')
c5 = Card('Th')

cset = CardSet([c4, c2, c3, c1, c5])
print "{0:b}".format(cset.get_bin())
flop_eval = FlopEvaluator(cset)

print cset

print flop_eval.get_made()

m = {
    "Straight Flush": 0,
    "Flush": 0,
    "Straight": 0,
    "Quads": 0,
    "Full House": 0,
    "Trips": 0,
    "Two Pair": 0,
    "Pair": 0,
    "High Card": 0,
}
i = 0
t = time.time()
table = basic_lut.read_table()
print "table read", time.time()-t

t2 = time.time()
for tab in table:
    string = table[tab]
print "dict test", time.time()-t2

combos = []
for c1, c2, c3, c4, c5 in combinations(product(STR_RANKS.keys(), STR_SUITS), 5):
    combos.append(CardSet([Card("".join(c1)),
                           Card("".join(c2)),
                           Card("".join(c3)),
                           Card("".join(c4)),
                           Card("".join(c5))
                           ])
                  )
print "combos done", time.time()-t

flops = []
for c in combos:
    flop_eval = FlopEvaluator(c)
    #flop_eval.use_table(table)
    flops.append(flop_eval)
print "flops done"
print t, time.time(), time.time()-t

t = time.time()
m = {
    "Straight Flush": 0,
    "Flush": 0,
    "Straight": 0,
    "Quads": 0,
    "Full House": 0,
    "Trips": 0,
    "Two Pair": 0,
    "Pair": 0,
    "High Card": 0,
}
for flop in flops:
    #i += 1
    made = flop.get_made()
    #m[made] += 1

print t, time.time(), time.time()-t
print i
for k, v in m.iteritems():
    print k, v
