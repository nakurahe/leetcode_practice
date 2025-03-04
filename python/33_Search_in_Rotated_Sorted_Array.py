class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # use binary search find the roatated pos
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid

        # now left and right should be the same, and
        # serves as the rotated pos

        if target < nums[0]:
            # start from rotated and len()-1
            start = left
            end = len(nums) - 1
        else:
            start = 0
            end = left

        while start <= end:
            mid = (start+end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid-1

        return -1


print(Solution().search([1, 3], 3))  # 1
