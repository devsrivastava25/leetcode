class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curr = 0
        best = 0
        for i in range(1,len(prices)):
            diff = prices[i] - prices[i-1]
            curr = max(0, curr + diff)
            best = max(best, curr)
        return best