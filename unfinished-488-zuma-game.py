from typing import List
from functools import reduce

class Solution:
    BALLS_UNIVERSUM = ['R','Y','B','G','W']
    BALLS_TO_COLLAPSE = 3

    class MaxDict(dict):
        def __setitem__(self, key, value):
            dict.__setitem__(self, key, max(value, self.get(key, 0)))

    class GameState:
        def __init__(self, board='', hand=''):
            self.board = board
            self.hand = hand

        def getHandBallsDict(self): 
            return { ball: self.hand.count(ball) for ball in Solution.BALLS_UNIVERSUM }
        
        def getSubsequentCountMax(self):
            tab = [1]
            subsequentCountMax = Solution.MaxDict()
            subsequentCountMax[self.board[0]] = 1
            for i, board in enumerate(zip(self.board[1:], self.board)):
                tab.append(tab[i-1] + 1 if board[0] == board[1] else 1)
                subsequentCountMax[board[0]] = tab[-1]
            return subsequentCountMax

        def isTerminal(self) -> bool:
            ballsHand = self.getHandBallsDict()
            ballsBoardSubsequent = self.getSubsequentCountMax()
            return reduce(max, [ ballsHand.get(ball, 0) + ballsBoardSubsequent.get(ball, 0) for ball in Solution.BALLS_UNIVERSUM ]) < Solution.BALLS_TO_COLLAPSE
        
        def insertBall(self, )

        def removeThrees(self, )

    def solve(self, gameState):
        

    def findMinStep(self, board: str, hand: str) -> int:
        gameState = self.GameState(board, hand)
        self.solve(gameState)
        print("isTerminal:", gameState.isTerminal())
        pass

def test(board, hand):
    print("TEST Board: {}, Hand: {}".format(board, hand))
    solution = Solution()
    print(solution.findMinStep(board, hand))

test("WRYB", "")
test("WRRBW", "RB")
test("WWRRBBWW", "WRBRW")
test("G", "GGGGG")
test("RBYYBBRRB","YRBGB")