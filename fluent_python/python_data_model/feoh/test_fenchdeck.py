import pytest
from frenchdeck import Card, FrenchDeck

@pytest.fixture
def my_deck():
    return FrenchDeck()

def test_standard_deck_card_count(my_deck):
    assert len(my_deck) == 52

def test_sequence_nature(my_deck):
    assert my_deck[51] == Card(rank='A', suit='hearts')
    assert my_deck[-20] == Card(rank='8', suit='clubs')

def test_out_of_bounds_index(my_deck):
   with pytest.raises(IndexError):
       bogus_card = my_deck[54]

def test_four_of_a_kind(my_deck):
    # Go for the gusto. Let's do 4 aces :)
    hand = [ card for card in my_deck if card.rank == 'A' ]
    assert len(hand) == 4