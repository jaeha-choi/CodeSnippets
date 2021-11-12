from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bots: List[int]) -> int:
        top, bot = tops[0], bots[0]
        topFlag = botFlag = True
        topCnt = [1, 0]
        botCnt = [0, 1]
        for currTop, currBot in zip(tops[1:], bots[1:]):
            if topFlag:
                if top == currTop and top != currBot:
                    topCnt[0] += 1
                if top == currBot and top != currTop:
                    topCnt[1] += 1
                if top != currTop and top != currBot:
                    topFlag = False

            if botFlag:
                if bot == currBot and bot != currTop:
                    botCnt[1] += 1
                if bot == currTop and bot != currBot:
                    botCnt[0] += 1
                if bot != currTop and bot != currBot:
                    botFlag = False

            if not topFlag and not botFlag:
                return -1

        # print(topFlag, topCnt)
        # print(botFlag, botCnt)

        if topFlag and botFlag:
            return min(min(topCnt), min(botCnt))
        elif topFlag:
            return min(topCnt)
        elif botFlag:
            return min(botCnt)
