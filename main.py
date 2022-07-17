import csv


class Card:
    def __init__(self, text, point_value):
        self.text = text
        self.point_value = point_value


class CardInfo:
    def __init__(self, text, quantity, point_value):
        self.text = text
        self.quantity = quantity
        self.point_value = point_value


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

print("Deck Length: " + str(len(deck)))

for item in deck:
    print(item.text, item.point_value)
