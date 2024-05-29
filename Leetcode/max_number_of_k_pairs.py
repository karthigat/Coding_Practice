#max_number_of_k_pairs

def max_pairs(nums, k):
    nums.sort()
    print(nums)
    l = 0
    r = len(nums) - 1
    count = 0
    while l<r:
        if nums[r]+nums[l] == k:
            count += 1
            r -= 1
            l += 1
        if nums[r]+nums[l] < k:
            l += 1
        if nums[r] + nums[l] > k:
            r -= 1
    return count
    
nums = [5,5,5,4,5]
k = 10

print(max_pairs(nums, k))