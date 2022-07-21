class Card:
    def __init__(self, text, point_value):
        self.text = text
        self.point_value = point_value


class CardInfo:
    def __init__(self, text, quantity, point_value):
        self.text = text
        self.quantity = quantity
        self.point_value = point_value

class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.scores = []
        self.total_score = 0

    def set_total_score(self):
        self.total_score = sum(self.scores)

class Game:
    def __init__(self, players, deck) -> None:
        self.players = players
        self.deck = deck
        self.discarded_cards = []
        self.round = 1
    
    def go_to_next_round(self):
        self.round += 1