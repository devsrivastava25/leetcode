class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {0:-1}
        r_sum = 0
        max_length = 0
        for i in range(len(nums)):
            r_sum += 1 if nums[i] == 1 else -1
            if r_sum in map:
                max_length = max(max_length,i-map[r_sum])
            else:
                map[r_sum] = i
        return max_length