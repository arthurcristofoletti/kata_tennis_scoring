class player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.advantage = False

    def update_score(self, new):
        print("before update score: ", self.score)
        self.score = new
        print("after update score: ", self.score)
    def player_name (self):
        #print(f"Player name is {self.name}")
        return self.name
    def player_score(self):
        #print(f"Player score is {self.score}")
        return self.score

class game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.deuce = False
        self.advantage = None
        self.winner = None

    def update_advantage(self, point_winner):
        self.advantage = point_winner

    def declare_winner(self, point_winner):
        self.winner = point_winner
        print(f"{point_winner} wins the game!")

    def update_player_score(self, point_winner):
        print ("point winner: ", point_winner)
        if point_winner == self.player1.player_name(): 
           print("match name point winner and player1")
           if self.player1.player_score() < 40:
             #print(f"updatescore for {point_winner}")
             print(f"access player1 score: {self.player1.player_score()}")
             print(f"next point for player1: {self.next_point(self.player1.player_score())}")
             self.player1.update_score(self.next_point(self.player1.player_score()))
             print(f"Player 1 score: {self.player1.player_score()}")
           elif self.player1.player_score() == 40:
             print("Player 1 has 40 points") 
             if self.player2.player_score() < 40:
              print("declare winner for player 1")
              self.declare_winner(point_winner)
        if point_winner == self.player2.player_name():
           print("match name point winner and player2") 
           if self.player2.player_score() < 40:
             #print(f"updatescore for {point_winner}")
             self.player2.update_score(self.next_point(self.player2.player_score()))
             print(f"Player 2 score: {self.player2.player_score()}")
           elif point_winner == self.player2.player_name() and self.player2.player_score() == 40 and self.player1.player_score() < 40:
             self.declare_winner(point_winner)
           elif self.check_deuce(self.player1, self.player2):
             self.deuce = True       

    def next_point(self, current_score):
        possible_scores = [0, 15, 30, 40]
        if current_score in possible_scores:
            print(f"Current score: {current_score}, next score: {possible_scores[possible_scores.index(current_score) + 1]}")
            return possible_scores[possible_scores.index(current_score) + 1]
        else:
            raise ValueError("Invalid score")

    def check_deuce(self, player1, player2):
        return player1.player_score() == 40 and player2.player_score() == 40

    def check_advantage(self):
        return self.advantage

    def update_game_score(self, player1, player2, point_winner ):
        print(f"Updating game score for point winner: {point_winner}")
        if player1.player_score() < 40 and player2.player_score() < 40:
            print(f"Updating score for {point_winner}")
            self.update_player_score(point_winner)
            if self.winner is not None:
                return
        elif player1.player_score() == 40 or player2.player_score() == 40:
             print("One of the players has 40 points")
             if self.check_deuce(player1, player2) and self.check_advantage() is None:
                print("Game is in deuce")
                self.update_advantage(point_winner)
             elif self.check_deuce(player1, player2) and self.check_advantage() == point_winner:
                print(f"{point_winner} wins the game from deuce")
                self.declare_winner(point_winner)
             elif self.check_deuce(player1, player2) and self.check_advantage() != point_winner:
                print("change advantage to other player")
                self.update_advantage(point_winner)
             else:
                print("one of the players is a winner")
                self.update_player_score(point_winner)

    def score_board(self):
        print(f"Score: {self.player1.player_name()} {self.player1.player_score()} - {self.player2.player_name()} {self.player2.player_score()}")
       
