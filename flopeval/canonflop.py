from flopeval.card import Card
from flopeval.constants import CHAR_SUITS

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
