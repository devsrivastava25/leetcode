class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n =len(arr)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i]+arr[i] #adding a base zero at the starting
        total = 0
        for length in range(1,n+1,2):
            for start in range(n-length+1):
                end = start+length
                # Sum of arr[start..end-1] in O(1)
                total += prefix[end] - prefix[start]
        return total