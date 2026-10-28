class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        length = len(s1)
        main = {}
        check = {}
        if len(s2) < len(s1):
           return False   
        for i in range(len(s1)):
            main[s1[i]] = main.get(s1[i],0)+1
        for i in range(len(s1)):
            check[s2[i]] = check.get(s2[i],0)+1
        if main == check:
            return True
        for i in range(len(s1),len(s2)):
            check[s2[i]] = check.get(s2[i],0)+1
            left = s2[i - length]
            check[left] -= 1
            if check[left]==0:
                del check[left]
            if main == check:
                return True
        return False
        