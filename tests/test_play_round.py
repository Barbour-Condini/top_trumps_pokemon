import pokefunctions as pokemon

# height, weight, speed, hp, attack, defense

def test_play_round_returns_dict():
    assert type(pokemon.play_round('height', [1], [2], [], True)) is dict

def test_play_round_height_emptyDraw_computerWins():
    round = pokemon.play_round('height', [1, 2, 3, 4], [5, 6, 7, 8], [], True)
    assert round['player_cards'] == [2, 3, 4]
    assert round['computer_cards'] == [6, 7, 8, 1, 5]
    assert round['player_choice'] == False

def test_play_round_height_singleCard_emptyDraw_computerWins():
    round = pokemon.play_round('height', [1], [5, 6, 7, 8], [], True)
    assert round['player_cards'] == []
    assert round['computer_cards'] == [6, 7, 8, 1, 5]
    assert round['player_choice'] == False

def test_play_round_height_PopulatedDraw_computerWins():
    round = pokemon.play_round('height', [1, 2, 3, 4], [5, 6, 7, 8], [9, 10], True)
    assert round['player_cards'] == [2, 3, 4]
    assert round['computer_cards'] == [6, 7, 8, 1, 5, 9, 10]
    assert round['draw_cards'] == []
    assert round['player_choice'] == False

def test_play_round_height_PopulatedDraw_playerWins():
    round = pokemon.play_round('hp', [1, 2, 3, 4], [7, 8, 9, 10], [11, 12], False)
    assert round['player_cards'] == [2, 3, 4, 7, 1, 11, 12]
    assert round['computer_cards'] == [8, 9, 10]
    assert round['draw_cards'] == []
    assert round['player_choice'] == True

def test_play_round_draw1():
    # attack is 49 for pokemon ids 1 and 152
    round1 = pokemon.play_round('attack', [1, 8, 3, 4], [152, 58, 7, 8], [], True)
    assert round1['player_cards'] == [8, 3, 4]
    assert round1['computer_cards'] == [58, 7, 8]
    assert round1['draw_cards'] == [1, 152]
    assert round1['player_choice'] == True


def test_play_round_draw2():
    # speed is 60 for pokemon ids 2 and 36
    round2 = pokemon.play_round('speed', [2, 3, 4], [36, 7, 8], [1, 152], True)
    assert round2['player_cards'] == [3, 4]
    assert round2['computer_cards'] == [7, 8]
    assert round2['draw_cards'] == [1, 152, 2, 36]
    assert round2['player_choice'] == True
