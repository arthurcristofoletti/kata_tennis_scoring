from src.app import player, game

def start_players():
    player1_name = input("Enter name for Player 1: ")
    player2_name = input("Enter name for Player 2: ")
    return player1_name, player2_name

def start_game(player1_name, player2_name):
    player1 = player(player1_name)
    player2 = player(player2_name)
    match = game(player1, player2)
    print(f"Game started between {player1_name} and {player2_name}")
    print(f"Initial score: {player1_name} {player1.score} - {player2_name} {player2.score}")
    print("Game in progress...")
    while match.winner is None:
        point_winner = input("Enter the name of the player who won the point (or 'exit' to quit): ")
        if point_winner.lower() == 'exit':
            print("Exiting the game.")
            break
        elif point_winner not in [player1_name, player2_name]:
            print("Invalid player name. Please try again.")
            continue
        print("Updating score... ")
        match.update_game_score(match.player1, match.player2, point_winner)
        print("game score updated")
        print("showing score board")
        match.score_board()
        print (match.winner)


if __name__ == "__main__":
    player1_name, player2_name = start_players()
    print(f"Players initialized: {player1_name} vs {player2_name}")
    start_game(player1_name, player2_name)