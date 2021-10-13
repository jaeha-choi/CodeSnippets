# Old answer
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for x, elem in enumerate(nums):
#             temp = target - elem
#             if temp in nums[:x]:
#                 return [x, nums[:x].index(temp)]
#             elif temp in nums[x + 1:]:
#                 return [x, nums[x + 1:].index(temp) + 1 + x]
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, elem in enumerate(nums):
            if (target - elem) in s:
                return [s[target - elem][0], i]
            else:
                s.setdefault(elem, [])
                s[elem].append(i)
