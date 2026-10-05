class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        n = len(gain)
        prefix = [0]
        count = 0
        for i in range(n):
            count += gain[i]
            prefix.append(count)
        return max(prefix)