# binary search algorithm

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        hi = len(nums) - 1
        lo = 0
        
        while(hi-lo > 1):
            mid = (hi+lo)//2 # calculate mid value
            if nums[mid] < target: # check if mid value is less than target
                lo = mid+1 # if so set low value to index after mid value
            else:  
                hi = mid # else set mid value as index
        if nums[lo] == target:
            return lo
        elif nums[hi] == target:
            return hi
        else:
            return -1


obj = Solution()
print(obj.search([-1,0,5], 2))