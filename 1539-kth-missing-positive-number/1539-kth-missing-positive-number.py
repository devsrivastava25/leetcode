class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        res = []
        n = arr[-1]+k+1
        for i in range(1,n):
            if i in arr:
                continue
            else:
                res.append(i)
        return res[k-1]
        