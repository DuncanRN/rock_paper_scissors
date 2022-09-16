class Game():

    def __init__(self, player_1, player_2):
        self.player_1=player_1
        self.player_2=player_2


    def who_wins(self):
        player_1 = self.player_1
        player_2 = self.player_2

        if player_1.choice == "rock":
            if player_2.choice == "rock":
                return None
            elif player_2.choice == "paper":
                return player_2
            elif player_2.choice == "scissors":
                return player_1
        elif player_1.choice == "paper":
            if player_2.choice == "rock":
                return player_1
            elif player_2.choice == "paper":
                return None
            elif player_2.choice == "scissors":
                return player_2
        elif player_1.choice == "scissors":
            if player_2.choice == "rock":
                return player_2
            elif player_2.choice == "paper":
                return player_1
            elif player_2.choice == "scissors":
                return None