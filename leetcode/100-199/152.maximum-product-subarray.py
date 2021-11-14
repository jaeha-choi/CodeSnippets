class Solution:
    def maxProduct(self, nums) -> int:
        mx = float("-inf")
        prev = neg = 1
        for num in nums:
            if num != 0:
                neg *= num
                mx = max(num, mx, neg, neg // prev)
                if prev > 0:
                    prev *= num
            else:
                mx = max(num, mx)
                neg = 1
                prev = 1

        return mx
