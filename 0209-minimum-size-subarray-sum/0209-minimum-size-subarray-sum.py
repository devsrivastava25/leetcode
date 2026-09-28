class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        sum = 0
        minV = float('inf')
        n = len(nums)
        for r in range (n):
            sum += nums[r]
            while sum>=target:
                minV = min(minV, r - l + 1)  # record BEFORE shrinking
                sum -= nums[l]
                l += 1
        return 0 if minV == float('inf') else minV

