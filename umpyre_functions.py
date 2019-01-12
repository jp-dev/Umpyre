"""
UMPYRE
Baseball functions for Umpyre game
"""

import random
import time

class TeamAtBat:
    def __init__(self, team):
        self.runs = 0
        self.outs = 0
        self.walks = 0
        self.team = team

    def team_at_bat(self):
        while self.outs < 3:
            self.player_at_bat()
        print(f"Runs for this at bat: {self.runs}\n\n\n")
        self.outs = 0  # Reset outs to zero after at bat
        return self.runs

    def player_at_bat(self):
        strikes = 0
        balls = 0

        while strikes < 3 and balls < 4:
            batter_swing = random.randint(0, 10)
            pitcher_throw = random.randint(0, 10)

            if pitcher_throw == batter_swing:
                # Batter hit the ball
                print(f"Throw is {pitcher_throw} - Swing is {batter_swing}")
                print(f"Batter hit the ball!")
                print("Hit result: Home Run! Yahoo!")
                self.runs += 1
                if self.walks > 0:
                    self.runs += self.walks  # Those previously walked will score
                    self.walks = 0  # Reset walks
                print(f"Runs: {self.runs}\n")
                # print("Advance base runners where needed\n")
                break
            elif pitcher_throw > batter_swing:
                # Pitch is a strike

                strikes += 1
                if strikes == 3:
                    self.outs += 1
                    print(f"Throw is {pitcher_throw} - Swing is {batter_swing} : Strike 3!\n")
                    print("You're out!\n")
                    print(f"Outs: {self.outs}\n")
                    break
                else:
                    print(f"Throw is {pitcher_throw} - Swing is {batter_swing} : Strike {strikes}\n")
            else:
                # Pitch is a ball
                balls += 1
                if balls == 4:
                    self.walks += 1
                    print(f"Throw is {pitcher_throw} - Swing is {batter_swing} : Ball 4!\n")
                    print("Walk! Take your base!")
                    print("Advance runners where needed\n")
                    if self.walks == 4:
                        self.runs += 1
                        self.walks = 0  # Reset walks
                        print("Extra run! Yee haw!")
                    break
                else:
                    print(f"Throw is {pitcher_throw} - Swing is {batter_swing}  :  Ball {balls}\n")

        print('=' * 50)
        print('\n\n')
        # time.sleep(2)


class Inning:
    def __init__(self, inning_num):
        self.inning_num = inning_num
        self.visiting_team_runs = 0
        self.home_team_runs = 0
        # Create other class instances from the __init__() function!
        self.visitors_atbat = TeamAtBat(team='Visitors')
        self.home_atbat = TeamAtBat(team='Hometeam')




