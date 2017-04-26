from flopeval.card import Card
from flopeval.constants import CHAR_SUITS
from itertools import combinations

def canon(board):
  """ Split cards by suit, then sort and relabel the suits.
      Flops that differ only in suits or ordering get mapped to a single flop"""
  suit_bucket = {}
  for card in board:
    suit_bucket.setdefault(Card.get_suit(card), []).append(Card.get_rank(card))
  result = []
  for suit, ranks in enumerate(sorted(suit_bucket.values())):
    for rank in ranks:
      result.append(Card.new(rank + CHAR_SUITS[suit]))
  return tuple(result)

if __name__ == '__main__':
    canon_flops = {}
    for flop in combinations(range(12), 3):
        canon_flops.setdefault(canon(flop), []).append(flop)
    print len(canon_flops.keys())
    for flop in sorted(canon_flops.keys()):
      print ''.join(map(Card.get_str, flop)), '->', [''.join(map(Card.get_str, x)) for x in canon_flops[flop]], len(canon_flops[flop])
