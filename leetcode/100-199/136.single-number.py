from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(0,len(nums),2):
        #     if i + 1 == len(nums) or nums[i] != nums[i+1]:
        #         return nums[i]

        return 2 * sum(set(nums)) - sum(nums)
