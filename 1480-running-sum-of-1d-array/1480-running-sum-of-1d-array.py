class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        count = 0
        prefix = []
        for i in range(n):
            count += nums[i]
            prefix.append(count)
        return prefix