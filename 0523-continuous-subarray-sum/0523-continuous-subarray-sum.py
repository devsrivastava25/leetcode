class Solution(object):
    def checkSubarraySum(self, nums, k):
        # remainder → earliest index where we saw it
        rem = {0: -1}
        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]
            r = prefix % k

            if r in rem:
                # subarray from rem[r]+1 to i has sum divisible by k
                # its length is i - rem[r]
                if i - rem[r] >= 2:
                    return True
            else:
                # only store the FIRST (earliest) index for this remainder
                rem[r] = i

        return False   