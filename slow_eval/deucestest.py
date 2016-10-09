from copy import deepcopy

from src import Card
from src import Deck
from src import Evaluator
from src import hand_range_to_cards

evaluator = Evaluator()
original_deck = Deck()


hands = hand_range_to_cards('random')

i = 0
for hand in hands:
    i += 1
    deck = deepcopy(original_deck)
    deck.draw_card(hand[0])
    deck.draw_card(hand[1])

    board = [
        deck.draw_rank('A'),
        deck.draw_rank('6'),
        deck.draw_rank('2')
    ]

    print evaluator.evaluate(hand, board),
    Card.print_pretty_cards(board + hand)

print i