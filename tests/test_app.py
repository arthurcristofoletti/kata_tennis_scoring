import pytest
from src.app import player, game
def test_player_initialization():
    p = player("Alice")
    assert p.name == "Alice"
    assert p.score == 0
    assert p.advantage == False
def test_player_score_update():
    p = player("Bob")
    p.update_score(15)
    assert p.score == 15
    p.update_score(30)
    assert p.score == 30    
def test_game_initialization():
    p1 = player("Alice")
    p2 = player("Bob")
    g = game(p1, p2)
    assert g.player1 == p1
    assert g.player2 == p2
    assert g.deuce == False
    assert g.advantage == None
    assert g.winner == None
def test_game_score_update():
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
    assert p1.score == 30
    assert p2.score == 15
    g.update_game_score(p1, p2, "Alice")
    assert p1.score == 40
    assert p2.score == 15
    g.update_game_score(p1, p2, "Bob")
    assert p1.score == 40
    assert p2.score == 30
    g.update_game_score(p1, p2, "Bob")
    assert p1.score == 40       
    assert p2.score == 40
    g.update_game_score(p1, p2, "Alice")
    assert g.deuce == True
    assert g.advantage == "Alice"
    g.update_game_score(p1, p2, "Bob")
    assert g.advantage == "Bob"
    g.update_game_score(p1, p2, "Bob")
    assert g.winner == "Bob"    

    
