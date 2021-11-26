from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        left, right = height[i], height[j]
        water = 0
        while i != j:
            if left < right:
                val = left
                curr = height[i + 1]
                left = max(curr, left)
                i += 1
            else:
                val = right
                curr = height[j - 1]
                right = max(curr, right)
                j -= 1
            if val - curr > 0:
                water += val - curr
        return water
