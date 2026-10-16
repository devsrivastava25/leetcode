class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        curr = best = nums[0]
        curr_min = minn = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            best = max(best, curr)
            curr_min = min(nums[i], curr_min + nums[i])
            minn = min(minn, curr_min)

        if best < 0:
            return best
        return max(best, total - minn)