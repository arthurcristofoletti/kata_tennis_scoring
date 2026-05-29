class player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.advantage = False

    def __str__(self):
        return f"{self.name} has a score of {self.score}"
    
class game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


    
    def next_point(self, current_score) -> int:
        possible_scores = [0, 15, 30, 40, "Deuce", "Advantage", "Win"]
        if current_score in possible_scores:
            return possible_scores[possible_scores.index(current_score) + 1]
        else:
            raise ValueError("Invalid score")

    def update_game_score(self, player1, player2, point_winner ):
        if player1.score == 3 and player2.score == 3:
            player1.score = "Deuce"
            player2.score = "Deuce"
        elif player1.score == 4 and player2.score == 3:
            player1.score = "Advantage"
        elif player1.score == 3 and player2.score == 4:
            player2.score = "Advantage"
        elif player1.score == 4 and player2.score < 3:
            player1.score = "Win"
        elif player2.score == 4 and player1.score < 3:
            player2.score = "Win"
        else:
            if point_winner == player1:
                player1.score = self.next_point(player1.score)
            else:
                player2.score = self.next_point(player2.score) 
        
    def show_score(self):
        return f"{self.player1.name}: {self.player1.score} - {self.player2.name}: {self.player2.score}"
    
        