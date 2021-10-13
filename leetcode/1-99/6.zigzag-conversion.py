class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = numRows
        ret = ""
        if n == 1:
            return s
        for idx in range(numRows):
            offset = idx * 2
            val = idx
            step = 2 * n - 2
            # print("offset: %s val: %s step: %s"%(offset, val, step))
            while val < len(s):

                if offset == 0:
                    ret += s[val]
                    val += step
                elif step == 0:
                    ret += s[val]
                    val += offset
                else:
                    ret += s[val]
                    val += step
                    if val < len(s):
                        ret += s[val]
                        val += offset
                # print(ret)
            n -= 1

        return ret
