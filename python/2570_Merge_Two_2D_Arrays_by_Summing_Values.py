from collections import deque


class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        res = []
        curr1 = nums1[0]
        curr2 = nums2[0]
        nums1 = deque(nums1[1:])
        nums2 = deque(nums2[1:])
        while curr1[0] != 1001 or curr2[0] != 1001:
            if curr1[0] < curr2[0]:
                res.append(curr1)
                curr1 = nums1.popleft() if nums1 else [1001, 0]
            elif curr1[0] > curr2[0]:
                res.append(curr2)
                curr2 = nums2.popleft() if nums2 else [1001, 0]
            else:
                res.append([curr1[0], curr1[1]+curr2[1]])
                curr1 = nums1.popleft() if nums1 else [1001, 0]
                curr2 = nums2.popleft() if nums2 else [1001, 0]

        return res


print(Solution().mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]))  # [[1, 6], [2, 3], [3, 2], [4, 6]]
