class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        running_sum = 0
        map = {0:1}
        answer = 0
        for num in nums:
            running_sum += num
            answer += map.get(running_sum-goal,0)
            map[running_sum] = map.get(running_sum,0)+1
        return answer