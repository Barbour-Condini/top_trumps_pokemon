import random
import requests


def card_allocation():
    """
    returns two lists of 16 integers, representing two card stacks.

    :return: (tuple) two lists of pokemon ids for the player and computer. Each id represents a pokemon card.
    """

    # initialise a list of pokemon ids, which represent the cards
    id_list = list(range(1, 200))

    # shuffle that list
    random.shuffle(id_list)

    # return the first 10 numbers of the shuffled list to the player,
    # and the 2nd 10 numbers of the list to the computer
    return id_list[0:10], id_list[10:20]


def collect_stats(pokemon_id):
    """"
    collects the stats of a selected pokemon from the pokeAPI.

    :param: pokemon_id: the id of the selected pokemon, representing the card at the top of the player or computer deck.
    :return: (list) Pokemon stats (name, height, weight, speed, hp, attack, defense)
    """

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        # 'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'speed': pokemon['stats'][5]['base_stat'],
        'hp': pokemon['stats'][0]['base_stat'],
        'attack': pokemon['stats'][1]['base_stat'],
        'defense': pokemon['stats'][2]['base_stat'],
    }
    

def play_round(selected_stat, player_cards, computer_cards, draw_cards, player_choice):
    """
    simulates 1 round of selecting a stat, comparing stats and reallocating cards.
    It calls two other functions: select_stat() adn card_reallocation()
    :params: 
        selected_stat: the pokemon stat that's been chosen for comparison between the player and computer cards
        player_cards; computer_cards: lists of pokemon ids that represent the player and computer card decks
        draw_cards: a list to hold any cards whose stats drew in earlier rounds
        player_choice: Boolean value that keeps track of whether it's the player's turn to select a stat, or the computer's
    :return: (dict) player_cards, computer_cards, draw_cards, player_choice
    """

    # identify and label player_stat and computer_stat
    player_stats = collect_stats(player_cards[0])
    computer_stats = collect_stats(computer_cards[0])

    player_stat = player_stats[selected_stat]
    computer_stat = computer_stats[selected_stat]

    if player_stat > computer_stat:
        reallocated_cards = card_reallocation(player_cards, computer_cards, draw_cards)
        player_cards = reallocated_cards[0]
        computer_cards = reallocated_cards[1]
        draw_cards.clear()
        player_choice = True
    elif computer_stat > player_stat:
        reallocated_cards = card_reallocation(computer_cards, player_cards, draw_cards)
        computer_cards = reallocated_cards[0]
        player_cards = reallocated_cards[1]
        draw_cards.clear()
        player_choice = False
    else:
        if len(player_cards) > 1:
            draw_cards.append(player_cards.pop(0))
        if len(computer_cards) > 1:
            draw_cards.append(computer_cards.pop(0))
    
    return {
        'player_cards': player_cards,
        'computer_cards': computer_cards,
        'draw_cards': draw_cards,
        'player_choice': player_choice
    }


def card_reallocation(winner_cards, loser_cards, draw_cards):
    """
    reallocates cards between the player and computer 
    after any stat comparison that didn't result in a draw
    :param:
        winner_cards, loser_cards: these represent the player/computer card decks
        draw_cards: a list that holds any cards whose stats drew in earlier rounds
    :return: (tuple) the reallocated card decks for the player and computer
    """
    # add both winner and loser cards to the back of the winner's card stack
    winner_cards.append(loser_cards[0])
    winner_cards.append(winner_cards[0])

    # remove the (already played and reallocated) top cards 
    # from both players' card stacks
    winner_cards.pop(0)
    loser_cards.pop(0)

    # add any drawn cards to the end of the winner's card stack
    for i in draw_cards:
        winner_cards.append(i)
    
    return winner_cards, loser_cards


def end_of_play(player_cards, computer_cards):
    """"
    return: (string) the winner/loser of the game 
    """

    if len(player_cards) > len(computer_cards):
        return 'You win!'
    elif len(computer_cards) > len(player_cards):
        return 'Computer wins! You have lost all your pokemon, trainer.'
