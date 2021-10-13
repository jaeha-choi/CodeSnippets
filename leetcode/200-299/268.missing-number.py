from typing import List


class Solution:
    # One could use "sum()" instead of looping through the list
    def missingNumber(self, nums: List[int]) -> int:
        totalSum = 0
        expectedSum = 0
        for i, elem in enumerate(nums):
            totalSum += elem
            expectedSum += i + 1
        return expectedSum - totalSum
