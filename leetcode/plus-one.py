class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += temp
            print(digits)
            if digits[i] >= 10:
                digits[i] -= 10
                temp = 1
            else:
                temp = 0
        if digits[0] >= 10:
            digits[0] -= 10
            temp = 1
        if temp:
            digits.insert(0, temp)
        return digits
