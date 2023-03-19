class Solution(object):
    def findPeakElement(self, nums):
        l,r = 0,len(nums)-1
        while l<=r-1:
            mid = (l+r)/2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                l = mid+1
            elif nums[mid] > nums[mid+1]:
                r = mid-1
        return l if nums[l] >= nums[r] else r