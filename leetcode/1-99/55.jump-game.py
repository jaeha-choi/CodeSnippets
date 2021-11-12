from typing import List


class Solution:

    # First attempt, inefficient
    # def canJump(self, nums: List[int]) -> bool:
    #     li = [False for i in range(len(nums))]
    #     li[-1] = True
    #     for i in range(len(nums)-2,-1,-1):
    #         for j in range(nums[i]):
    #             if li[i+j+1]:
    #                 li[i] = True
    #                 break
    #     return li[0]

    def canJump(self, nums: List[int]) -> bool:
        res = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= res:
                res = i
        return res == 0
