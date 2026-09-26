class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        constant = 1
        count = 0
        n = len(nums)
        for right in range(left,n):
           constant = constant*nums[right]
           while left <= right and  constant >= k :
                constant = constant//nums[left]
                left += 1
           count += (right-left+1)
            
        return count
      