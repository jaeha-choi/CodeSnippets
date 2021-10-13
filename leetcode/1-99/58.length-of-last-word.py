class Solution:
    # def lengthOfLastWord(self, s: str) -> int:
    #     return len(s.split()[-1])

    # Answer without using .split()
    def lengthOfLastWord(self, s: str) -> int:
        end = start = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " " and end == -1:
                end = i
            elif s[i] == " " and end != -1:
                start = i
                break
        return end - start
