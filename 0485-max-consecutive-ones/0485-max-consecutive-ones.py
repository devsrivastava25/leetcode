class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_count = 0
        max_ans = current_count
        j = 0
        n = len(nums)
        while j<n:
            if nums[j] == 1:
                current_count += 1
            else:
                max_ans = max(max_ans,current_count)
                current_count = 0
            j += 1
        max_ans = max(max_ans, current_count)
        return max_ans
