import csv
import random

from model import Card, CardInfo


def get_deck():
    deck_json = {}

    with open("deckStructure.csv") as csvFile:
        rows = csv.reader(csvFile)
        for idx, row in enumerate(rows):
            if idx != 0:
                cardInfo = CardInfo(row[0], int(row[2]), int(row[1]))
                deck_json.update({str(row[0]): cardInfo})

    deck = []
    for item in deck_json.items():
        cardInfo = item[1]
        text = cardInfo.text
        point_value = cardInfo.point_value
        quantity = cardInfo.quantity
        for card_to_build in range(quantity):
            deck.append(Card(text, point_value))
        
    shuffledDeck = deck.copy()
    random.shuffle(shuffledDeck)
    return shuffledDeck

def print_deck(deck):
    for idx, card in enumerate(deck):
        if idx % 8 == 0:
            print('\n')
        print("[" + card.text + ", " + str(card.point_value) + "]", end=", ")
    print('\n')
