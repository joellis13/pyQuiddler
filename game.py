from deck_stuff import get_deck
from model import Game
from playaz import get_players

def set_up_game():
    players = get_players()
    deck = get_deck()
    return Game(players, deck)
