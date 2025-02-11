import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # store all points into a heap queue
        # until there are k elements in the q,
        # pop the largest to keep the length until the end.

        q = []
        for point in points:
            # need to pop so store from the farthest.
            heapq.heappush(q, (-(point[0]**2 + point[1]**2)**0.5, point))
            if len(q) > k:
                heapq.heappop(q)

        return [x[1] for x in q[::-1]]


print(Solution().kClosest([[-95,76],[17,7],[-55,-58],[53,20],[-69,-8],[-57,87],[-2,-42],[-10,-87],[-36,-57],[97,-39],[97,49]], 5))  # [[-2,-42],[10,-87],[-36,-57],[-55,-58],[17,7]]
