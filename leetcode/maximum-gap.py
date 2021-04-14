class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        diff = nums[1] - nums[0]

        for i in range(len(nums) - 1):
            curr = nums[i + 1] - nums[i]
            if diff < curr:
                diff = curr
        return diff
