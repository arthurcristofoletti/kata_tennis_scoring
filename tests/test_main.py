from src.main import start_players, start_game
def test_start_players(monkeypatch):
    inputs = iter(["Alice", "Bob"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    player1_name, player2_name = start_players()
    assert player1_name == "Alice"
    assert player2_name == "Bob"
def test_start_game(monkeypatch):
    inputs = iter(["Alice", "Bob", "Alice", "Bob", "Alice", "Bob", "Alice", "Bob", "Alice", "Bob", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    player1_name, player2_name = start_players()
    start_game(player1_name, player2_name)

