class Solution:
    def reverse(self, x: int) -> int:
        ############################################
        # Solution using conversion
        INT_MAX = 2147483648
        newX = "".join(reversed(str(abs(x))))

        if len(newX) < len(str(INT_MAX)):
            if x < 0:
                return int("-" + newX)
            return int(newX)

        elif len(newX) == len(str(INT_MAX)):
            if x < 0 and newX <= str(INT_MAX - 1):
                return int("-" + newX)
            elif newX <= str(INT_MAX):
                return int(newX)
        return 0

        ############################################
        # Solution without converting to string
        import math

        if x == 0:
            return 0

        # Both variables don't include the most significant bit
        INT_MAX = 147483647
        INT_MIN_NO_SIGN = 147483648

        y = abs(x)

        res = 0
        sig = (y % 10)
        sig_multiplier = (10 ** math.floor(math.log10(y)))
        y //= 10
        i = 0

        while y >= 10:
            res += (y % 10) * (10 ** math.floor(math.log10(y)))
            y //= 10
            i += 1

        res += (y % 10)

        if sig < 2 or i < 8:
            res += sig * sig_multiplier
            if x < 0:
                return res * -1
            else:
                return res
        if sig == 2:
            if x < 0 and INT_MIN_NO_SIGN - res >= 0:
                return (sig * sig_multiplier + res) * -1
            elif x >= 0 and INT_MAX - res >= 0:
                return sig * sig_multiplier + res
        return 0
