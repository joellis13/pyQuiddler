from deck_stuff import get_deck, print_deck
from game import set_up_game
from playaz import print_player_scores

game = set_up_game()
print_player_scores(game.players)