# 2020-05-13
# https://leetcode.com/problems/word-pattern/
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Example 1:
#
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
#
# Example 2:
#
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
#
# Example 3:
#
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
#
# Example 4:
#
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
#
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        newL = {}
        i = 0

        if len(pattern) != len(s):
            return False

        for letter in pattern:
            if not letter in newL:
                newL[letter] = s[i]
            else:
                if newL[letter] != s[i]:
                    return False
            i += 1

        flipped = {}
        for key, value in newL.items():
            if value not in flipped:
                flipped[value] = [key]
            else:
                return False

        return True
