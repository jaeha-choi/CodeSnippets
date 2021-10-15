from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = []
        curr = 1
        for num in nums[::-1]:
            curr *= num
            answers.append(curr)

        curr = 1
        for i in range(len(nums) - 1, 0, -1):
            answers[i] = curr * answers[i - 1]
            curr *= nums[-(i + 1)]
        answers[0] = curr
        return answers[::-1]
