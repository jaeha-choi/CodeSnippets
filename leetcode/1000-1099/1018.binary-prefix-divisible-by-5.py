from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        x = 0
        for i, elem in enumerate(nums):
            x = x << 1
            x += elem
            nums[i] = x % 5 == 0
        return nums
