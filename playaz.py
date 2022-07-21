from model import Player


def get_players():
    number_of_players = int(input('\nNumber of players => '))

    players = []
    for idx in range(number_of_players):
        name = input('Player ' + str(idx) + ' name => ')
        players.append(Player(idx +1, name))
    
    return players

def print_player_scores(players):
    for player in players:
        print('\n' + player.name)
        print('  Scores:', player.scores)
        print('  Total Score:', player.total_score)

