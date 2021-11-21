class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        strstack = []
        n = ""
        ret = ""
        for i, char in enumerate(s):
            if char.isdigit():
                n += char
            elif char == "[":
                stack.append(int(n))
                strstack.append("")
                n = ""
            elif char == "]":
                string = strstack.pop() * stack.pop()
                if len(stack) != 0:
                    strstack[-1] += string
                else:
                    ret += string
            elif len(stack) > 0:
                strstack[-1] += char
            else:
                ret += char
        return ret
