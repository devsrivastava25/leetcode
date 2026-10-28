class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        def expand(l, r):
            c = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                c += 1
                l -= 1
                r += 1
            return c

        for i in range(len(s)):
            count += expand(i, i)
            count += expand(i, i+1)
        return count