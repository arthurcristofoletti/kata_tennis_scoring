import pytest
from src.app import player, game
def test_player_initialization():
    p = player("Alice")
    assert p.name == "Alice"
    assert p.score == 0
    assert p.advantage == False 
def test_game_initialization():
    p1 = player("Alice")
    p2 = player("Bob")
    g = game(p1, p2)
    assert g.player1.name == "Alice"
    assert g.player2.name == "Bob"
    assert g.player1.score == 0
    assert g.player2.score == 0
def test_next_point():      
    p1 = player("Alice")
    p2 = player("Bob")
    g = game(p1, p2)
    assert g.next_point(0) == 15
    assert g.next_point(15) == 30
    assert g.next_point(30) == 40
    with pytest.raises(ValueError):
        g.next_point(50)
def test_update_game_score():   
    p1 = player("Alice")
    p2 = player("Bob")
    g = game(p1, p2)
    
    g.update_game_score(p1, p2, "Alice")
    assert p1.score == 15
    assert p2.score == 0
    
    g.update_game_score(p1, p2, "Bob")
    assert p1.score == 15
    assert p2.score == 15
    
    g.update_game_score(p1, p2, "Alice")
    g.update_game_score(p1, p2, "Alice")
    assert p1.score == 40
    assert p2.score == 15
    
    g.update_game_score(p1, p2, "Bob")
    g.update_game_score(p1, p2, "Bob")
    assert p1.score == "Deuce"
    assert p2.score == "Deuce"
    
    g.update_game_score(p1, p2, "Alice")
    assert p1.score == "Advantage"
    assert p2.score == "Deuce"
    
    g.update_game_score(p1, p2, "Alice")
    assert p1.score == "Win"    
    assert p2.score == "Deuce"  

    
