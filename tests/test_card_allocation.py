import pokefunctions as pokemon

def test_card_allocation_10_per_player():
    assert len(pokemon.card_allocation()[0]) == 10
    assert len(pokemon.card_allocation()[0]) == len(pokemon.card_allocation()[1]) 

def test_card_allocation_distinct_decks():
    assert pokemon.card_allocation()[0] != pokemon.card_allocation()[1]

def test_card_allocation_no_card_duplicates():
    test = pokemon.card_allocation()
    for i in test[0]:
        assert i not in test[1]