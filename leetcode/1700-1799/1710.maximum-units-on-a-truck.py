from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse=True, key=lambda x: x[1])
        space = truckSize
        acc = 0
        for box in boxTypes:
            if space - box[0] >= 0:
                space -= box[0]
                acc += box[0] * box[1]
            else:
                acc += box[1] * space
                break
        return acc

# Time: O(n log n)
# Space: O(1)
