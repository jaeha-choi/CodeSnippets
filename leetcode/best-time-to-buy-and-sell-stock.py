from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        buy = prices[0]
        for elem in prices:
            if elem < buy:
                buy = elem
            elif elem - buy > mx:
                mx = elem - buy
        return mx
