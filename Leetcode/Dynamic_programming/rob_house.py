def rob(idx, nums):
    if idx < 0:
        return 0

    rob_house = nums[idx] + rob(idx-2, nums)

    non_rob = rob(idx-1, nums)
    return max(rob_house, non_rob)

nums = [2,3,4,5]
idx = len(nums)-1
print(rob(idx, nums))
