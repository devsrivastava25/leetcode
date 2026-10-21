class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = nums[0]
        maxx = nums[0]
        curr_min = nums[0]
        minn = nums[0]
        
        for i in range(1,len(nums)):
            curr_max = max(nums[i],curr_max+nums[i])
            maxx = max(maxx,curr_max)
            curr_min = min(nums[i],curr_min+nums[i])
            minn = min(minn,curr_min)
        answer = max(abs(maxx),abs(minn))
        return answer