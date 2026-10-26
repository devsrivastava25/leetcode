class Solution(object):
    def validPalindrome(self, s):
        arr = [ch.lower() for ch in s if ch.isalnum()]
        
        def is_pal(l, r):
            while l < r:
                if arr[l] != arr[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        start, end = 0, len(arr) - 1
        while start < end:
            if arr[start] != arr[end]:
                return is_pal(start + 1, end) or is_pal(start, end - 1)
            start += 1
            end -= 1
        return True   