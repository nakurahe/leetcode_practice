class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])

        res = []
        i = 1
        while i < len(intervals):
            buffer_list = []
            if intervals[i-1][-1] >= intervals[i][0]:
                buffer_list.append(min(intervals[i-1][0], intervals[i][0]))
                buffer_list.append(max(intervals[i-1][-1], intervals[i][-1]))
                res.append(buffer_list)
                intervals.pop(i-1)
                intervals.pop(i-1)
                intervals.insert(i-1, buffer_list)
            else:
                if intervals[i-1] not in res:
                    res.append(intervals[i-1])
                res.append(intervals[i])
                i += 1

        return res


print(Solution().merge([[1, 4], [0, 2], [3, 5]]))  # [[0,5]]
