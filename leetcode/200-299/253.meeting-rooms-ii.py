import heapq


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        li = [0]

        for start, end in sorted(intervals, key=lambda x: x[0]):
            if start >= li[0]:
                heapq.heappushpop(li, end)
            else:
                heapq.heappush(li, end)

        return len(li)
