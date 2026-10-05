class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix = 0
        m = {0: 1}

        for num in nums:
            prefix += num
            count += m.get(prefix - k, 0)
            m[prefix] = m.get(prefix, 0) + 1

        return count   