from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    # Inplace
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     nums.sort()
    #     temp = nums[0]
    #     for x in nums[1:]:
    #         if temp == x:
    #             return True
    #         temp = x
    #     return False
