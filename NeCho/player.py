from NeCho.helper import *


class Spot:
    def __init__(self, colour, n):
        self.colour = colour
        self.n = n
        self.targets = []


class ExamplePlayer:
    def __init__(self, colour):
        self.colour = colour
        self.board = \
            [[Spot("black", 1) if ((y == 6 or y == 7) and (x != 2 and x != 5))
              else Spot("white", 1) if ((y == 0 or y == 1) and (x != 2 and x != 5))
            else None for y in range(8)] for x in range(8)]

        self.black = [(0, 7), (1, 7), (3, 7), (4, 7), (6, 7), (7, 7), (0, 6), (1, 6), (3, 6), (4, 6), (6, 6), (7, 6)]
        self.white = [(0, 1), (1, 1), (3, 1), (4, 1), (6, 1), (7, 1), (0, 0), (1, 0), (3, 0), (4, 0), (6, 0), (7, 0)]

    def action(self):
        """
        This method is called at the beginning of each of your turns to request 
        a choice of action from your program.

        Based on the current state of the game, your player should select and 
        return an allowed action to play on this turn. The action must be
        represented based on the spec's instructions for representing actions.
        """
        # TODO: Decide what action to take, and return it
        return "BOOM", getattr(self, self.colour)[0]

    def update(self, colour, action):
        """
        This method is called at the end of every turn (including your player’s 
        turns) to inform your player about the most recent action. You should 
        use this opportunity to maintain your internal representation of the 
        game state and any other information about the game you are storing.

        The parameter colour will be a string representing the player whose turn
        it is (White or Black). The value will be one of the strings "white" or
        "black" correspondingly.

        The parameter action is a representation of the most recent action
        conforming to the spec's instructions for representing actions.

        You may assume that action will always correspond to an allowed action 
        for the player colour (your method does not need to validate the action
        against the game rules).
        """
        # TODO: Update state representation in response to action.

        if action[0] == 'BOOM':
            boom(self.board, action[1], self.black, self.white)
