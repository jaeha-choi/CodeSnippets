class Solution:
    # First attempt
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     unique = set()
    #     left = mx = 0
    #     for right, char in enumerate(s):
    #         if char in unique:
    #             while char in unique:
    #                 unique.remove(s[left])
    #                 left += 1
    #         unique.add(char)
    #         mx = max(mx, right - left + 1)
    #     return mx

    # Second attempt
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = {}
        left = mx = 0
        for idx, char in enumerate(s):
            if char in unique and left <= unique[char]:
                left = unique[char] + 1
            unique[char] = idx
            mx = max(mx, idx - left + 1)
        return mx
