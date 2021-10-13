from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        abs_mx = nums[0]
        for i in range(1, len(nums)):
            mx = max(mx + nums[i], nums[i])
            if mx > abs_mx:
                abs_mx = mx
        return abs_mx
