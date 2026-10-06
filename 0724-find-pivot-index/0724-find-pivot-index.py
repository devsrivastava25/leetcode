class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)
        prefix = [0] * n          # FIX 1: was []*0
        suffix = [0] * n          # FIX 1: was []*0
        prefix_sum = 0
        suffix_sum = 0
        for i in range(n):
            prefix[i] = prefix_sum
            prefix_sum += nums[i]
        for i in range(n-1, -1, -1):
            suffix[i] = suffix_sum
            suffix_sum += nums[i]
        for i in range(n):
            left_sum = prefix[i]  # FIX 2: was prefix[i-1]
            right_sum = suffix[i] # FIX 3: was suffix[i+1]
            if left_sum == right_sum:
                return i
        return -1   