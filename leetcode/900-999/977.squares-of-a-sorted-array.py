from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = end = 0
        res = []
        for i, elem in enumerate(nums):
            start = end = i
            if 0 <= elem:
                break
        start -= 1
        while 0 <= start or end < len(nums):
            neg = pos = float("inf")
            if 0 <= start:
                neg = abs(nums[start])
            if start != end and end < len(nums):
                pos = nums[end]

            if neg <= pos:
                res.append(neg ** 2)
                start -= 1
            else:
                res.append(pos ** 2)
                end += 1
        return res
