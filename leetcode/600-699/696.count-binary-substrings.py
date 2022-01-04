class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ret = switch = zero = one = 0
        prevChar = s[0]

        for char in s:
            if prevChar != char:
                switch += 1
                if switch % 2 == 0:
                    ret += min(zero, one)
                    if prevChar == "1":
                        zero = 0
                    else:
                        one = 0
                    switch = 1
            if char == "0":
                zero += 1
            elif char == "1":
                one += 1
            prevChar = char

        ret += min(zero, one)
        return ret
