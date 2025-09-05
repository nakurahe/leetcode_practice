def sortColors(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    red = white = 0
    blue = len(nums) - 1

    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[blue], nums[white] = nums[white], nums[blue]
            blue -= 1


sortColors([2, 0, 2, 1, 1, 0])
