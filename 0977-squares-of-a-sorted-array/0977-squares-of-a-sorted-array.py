class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        start, last = 0, n - 1
        result = [0] * n
        pos = n - 1

        while start <= last:
            if abs(nums[start]) > abs(nums[last]):
                result[pos] = nums[start] ** 2
                start += 1
            else:
                result[pos] = nums[last] ** 2
                last -= 1
            pos -= 1  

        return result   