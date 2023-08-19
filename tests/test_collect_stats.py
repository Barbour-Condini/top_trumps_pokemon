import pokefunctions as pokemon

def test_collect_stats_returns_dictionary():
    assert type(pokemon.collect_stats(10)) is dict

def test_collect_stats_name():
    assert pokemon.collect_stats(1)['name'] == "bulbasaur"
    assert pokemon.collect_stats(90)['name'] == "shellder"

def test_collect_stats_height():
    assert pokemon.collect_stats(12)['height'] == 11
    assert pokemon.collect_stats(90)['height'] == 3

def test_collect_stats_weight():
    assert pokemon.collect_stats(121)['weight'] == 800
    assert pokemon.collect_stats(90)['weight'] == 40

def test_collect_stats_speed():
    assert pokemon.collect_stats(178)['speed'] == 95
    assert pokemon.collect_stats(90)['speed'] == 40

def test_collect_stats_hp():
    assert pokemon.collect_stats(26)['hp'] == 60
    assert pokemon.collect_stats(90)['hp'] == 30

def test_collect_stats_attack():
    assert pokemon.collect_stats(3)['attack'] == 82
    assert pokemon.collect_stats(90)['attack'] == 65

def test_collect_stats_defense():
    assert pokemon.collect_stats(88)['defense'] == 50
    assert pokemon.collect_stats(90)['defense'] == 100