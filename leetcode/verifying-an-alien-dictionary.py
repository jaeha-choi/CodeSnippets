from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i, char in enumerate(order):
            d[char] = i
        print(d)
        i = 0

        while i < len(words) - 1:
            check = True
            for ch1, ch2 in zip(words[i], words[i + 1]):
                if d[ch1] > d[ch2]:
                    return False
                elif d[ch1] < d[ch2]:
                    check = False
                    break
            if check and len(words[i]) > len(words[i + 1]):
                return False

            i += 1
        return True
