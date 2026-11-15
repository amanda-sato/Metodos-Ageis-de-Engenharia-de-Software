class TennisGame1:
    SCORE_NAMES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        if self.p1points == self.p2points:
            if self.p1points >= 3:
                return "Deuce"
            else:
                return self.SCORE_NAMES[self.p1points] + "-All"
        elif self.p1points >= 4 or self.p2points >= 4:
            minus_result = self.p1points - self.p2points
            if minus_result == 1:
                return "Advantage " + self.player1_name
            elif minus_result == -1:
                return "Advantage " + self.player2_name
            elif minus_result >= 2:
                return "Win for " + self.player1_name
            else:
                return "Win for " + self.player2_name
        else:
            return self.SCORE_NAMES[self.p1points] + "-" + self.SCORE_NAMES[self.p2points]