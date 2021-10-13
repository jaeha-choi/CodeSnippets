from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Method 1 (works but does not answer the question)
        # i = 0
        # while i < len(nums):
        #     if nums[i] == val:
        #         del nums[i]
        #         i -= 1
        #     i += 1
        # return i

        i = 0
        k = 1
        while i <= len(nums) - k:
            if nums[i] == val:
                while nums[-k] == val:
                    if k == len(nums) - i:
                        return len(nums) - k
                    k += 1
                nums[i] = nums[-k]
                k += 1
            i += 1
            print(i, k, nums)
        return len(nums) - k + 1

        # i = 0
        # k = len(nums)
        # while i < k:
        #     if nums[i] == val:
        #         nums[i] = nums[k-1]
        #         k -= 1
        #     else:
        #         i += 1
        # return i
