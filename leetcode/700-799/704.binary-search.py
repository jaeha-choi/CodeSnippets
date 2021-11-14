from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        si = len(nums) // 2
        if nums[si] == target:
            return si
        if target < nums[si]:
            return self.search(nums[:si], target)
        else:
            val = self.search(nums[si + 1:], target)
            if val == -1:
                return val
            return val + si + 1
