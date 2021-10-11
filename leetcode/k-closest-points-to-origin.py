import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        li = []
        for elem in points:
            li.append(math.sqrt(elem[0] ** 2 + elem[1] ** 2))

        res = []
        val = []
        for i, elem in enumerate(li):
            if len(res) < k:
                res.append(points[i])
                val.append(elem)
            else:
                mx = max(val)
                if mx > elem:
                    idx = val.index(mx)
                    res[idx] = points[i]
                    val[idx] = elem
        return res
