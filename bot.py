# Hello! Need help getting started? Check out the Four in a Row tutorial:
# 👉 https://github.com/zilch/beta/blob/main/docs/games/four-in-a-row/tutorial.md
import random
class FourInARowBot:
    def __init__(self, config):
        # 👇 Get started by uncommenting this line
        # print("Hello World!", config)
        pass

    def move(self, previous_moves):
        print(previous_moves) # array with previous moves by player one and two
        move = random.randint(0,6)
        #if(previous_moves[-1]=5):
        #    move = 4
        # Return column you'd like to move here.
        # Value should be integer between 0 and 6
        return move
