from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        li = [float("inf") for i in range(len(nums))]
        li[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            jump = nums[i]
            if i + jump + 1 > len(nums):
                li[i] = min(li[i:]) + 1
            else:
                li[i] = min(li[i:i + jump + 1]) + 1
        return li[0]
