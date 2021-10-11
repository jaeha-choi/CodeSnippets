import heapq
from typing import List


# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         li = []
#         for elem in points:
#             li.append(math.sqrt(elem[0] ** 2 + elem[1] ** 2))
#
#         res = []
#         val = []
#         for i, elem in enumerate(li):
#             if len(res) < k:
#                 res.append(points[i])
#                 val.append(elem)
#             else:
#                 mx = max(val)
#                 if mx > elem:
#                     idx = val.index(mx)
#                     res[idx] = points[i]
#                     val[idx] = elem
#         return res

# Second attempt
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         li = []
#         for i, (x, y) in enumerate(points):
#             val = x ** 2 + y ** 2
#             li.append([val, i])
#         return [points[i[1]] for i in sorted(li, key=lambda z: z[0])[:k]]

# Third attempt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, (x, y) in enumerate(points):
            heapq.heappush(heap, (-(x ** 2 + y ** 2), (x, y)))
            if len(heap) - 1 == k:
                heapq.heappop(heap)
        return [elem[1] for elem in heap]
