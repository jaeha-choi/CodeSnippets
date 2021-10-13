class Solution:
    # 1. No DP
    def climbStairs1(self, n: int) -> int:
        import math

        total = 1  # 1111
        one = n % 2
        two = n // 2
        while 0 < two:
            total += math.factorial(one + two) // (math.factorial(one) * math.factorial(two))
            two -= 1
            one += 2
        return total

    # 2. DP, iterative
    def climbStairs(self, n: int) -> int:
        d = {0: 1, 1: 1}

        def dp_fact(n):
            while n not in d:
                d[len(d)] = len(d) * d[len(d) - 1]
            return d[n]

        total = 1  # 1111
        one = n % 2
        two = n // 2
        while 0 < two:
            total += dp_fact(one + two) // (dp_fact(one) * dp_fact(two))
            two -= 1
            one += 2
        return total
