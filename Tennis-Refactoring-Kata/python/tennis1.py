class TennisGame1:
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
        result = ""
        if self.p1points == self.p2points:
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")
        elif self.p1points >= 4 or self.p2points >= 4:
            minus_result = self.p1points - self.p2points
            if minus_result == 1:
                result = "Advantage " + self.player1_name
            elif minus_result == -1:
                result = "Advantage " + self.player2_name
            elif minus_result >= 2:
                result = "Win for " + self.player1_name
            else:
                result = "Win for " + self.player2_name
        else:
            result = (
                {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}[self.p1points]
                + "-"
                + {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}[self.p2points]
            )
        return result