from typing import List


class Solution:
    # Recursive solution with O(log n) complexity
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] >= target:
            return 0
        elif len(nums) == 1 and nums[0] < target:
            return 1
        elif target <= nums[len(nums)//2-1]:
            idx = self.searchInsert(nums[:len(nums)//2], target)
        elif target >= nums[len(nums)//2]:
            idx = len(nums)//2
            idx += self.searchInsert(nums[len(nums)//2:], target)
        else:
            return len(nums)//2
        return idx
