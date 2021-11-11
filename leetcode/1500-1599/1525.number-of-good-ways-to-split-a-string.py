from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        s1 = Counter()
        s2 = Counter(s)
        cnt = 0
        for elem in s:
            if len(s1) == len(s2):
                cnt += 1
            # s1.setdefault(elem, 0)
            s1[elem] += 1
            s2[elem] -= 1
            if s2[elem] == 0:
                del s2[elem]

        return cnt
