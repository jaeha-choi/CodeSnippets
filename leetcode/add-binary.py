class Solution:
    def addBinary(self, a: str, b: str) -> str:
        string = str(int(a) + int(b))
        carry = 0
        for i in range(len(string) - 1, -1, -1):
            val = int(string[i]) + carry
            carry = 0
            if val > 1:
                val -= 2
                carry = 1
            string = string[:i] + str(val) + string[i + 1:]
        if carry:
            return "1" + string
        return string
