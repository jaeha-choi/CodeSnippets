from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zero = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                count_zero += 1
                del nums[i]
            else:
                i += 1
        for x in range(count_zero):
            nums.append(0)
