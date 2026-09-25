class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        off_count = 0
        longest = 0
        n = len(nums)

        for right in range(n):
            if nums[right] == 0:
                off_count += 1           

            if off_count > k:            
                if nums[left] == 0:
                    off_count -= 1       
                left += 1                

            longest = max(longest, right - left + 1)  

        return longest   