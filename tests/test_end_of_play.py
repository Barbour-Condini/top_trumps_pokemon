import pokefunctions as pokemon

def test_end_of_play_win():
    computer_cards = []
    player_cards = [1, 2, 3, 4]
    assert pokemon.end_of_play(player_cards, computer_cards) == 'You win!'

def test_end_of_play_lose():
    computer_cards = [1, 2, 3, 4]
    player_cards = []
    assert pokemon.end_of_play(player_cards, computer_cards) == 'Computer wins! You have lost all your pokemon, trainer.'