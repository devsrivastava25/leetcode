class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = [ch.lower() for ch in s if ch.isalnum()]
        n = len(arr)
        answer = arr[:]
        start = 0
        end = n-1
        while start<=end:
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -= 1
        return(arr == answer)