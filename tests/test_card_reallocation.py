import pokefunctions as pokemon

def test_card_reallocation_empty_draw():
    player_cards, computer_cards = pokemon.card_allocation()
    draw_cards = []
    for i in range(5):
        reallocated_cards = pokemon.card_reallocation(player_cards, computer_cards, draw_cards)
    assert len(reallocated_cards[0]) == len(player_cards) == 15
    assert len(reallocated_cards[1]) == len(computer_cards) == 5

    for i in range(2):
        reallocated_cards = pokemon.card_reallocation(computer_cards, player_cards, draw_cards)
    assert len(reallocated_cards[0]) == len(computer_cards) == 7
    assert len(reallocated_cards[1]) == len(player_cards) == 13


def test_card_reallocation_populated_draw():
    player_cards, computer_cards = pokemon.card_allocation()
    draw_cards = [1, 2, 3, 4]
    reallocated_cards = pokemon.card_reallocation(player_cards, computer_cards, draw_cards)
    assert len(reallocated_cards[0]) == len(player_cards) == 15
    assert len(reallocated_cards[1]) == len(computer_cards) == 9

    draw_cards = [5, 6]
    reallocated_cards = pokemon.card_reallocation(computer_cards, player_cards, draw_cards)
    assert len(reallocated_cards[0]) == len(computer_cards) == 12
    assert len(reallocated_cards[1]) == len(player_cards) == 14