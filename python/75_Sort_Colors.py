# no such key error waiting to be fixed
def sortColors(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    color_dict = {}
    for num in nums:
        if num in color_dict:
            color_dict[num] += 1
        else:
            color_dict[num] = 1

    nums[0: color_dict[0]] = [0] * color_dict[0]
    nums[color_dict[0]: color_dict[0]+color_dict[1]] = [1] * color_dict[1]
    nums[color_dict[0]+color_dict[1]:] = [2] * color_dict[2]


sortColors([2, 0, 2, 1, 1, 0])
