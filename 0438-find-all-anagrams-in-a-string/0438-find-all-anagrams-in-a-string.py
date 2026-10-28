class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        length = len(p)
        if len(s) < length:
          return []   
        main = {}
        check = {}
        answer = []
        for i in range(len(p)):
            main[p[i]] = main.get(p[i],0)+1
        for i in range(length):
            check[s[i]] = check.get(s[i],0)+1
        if main == check:
            answer.append(0)
        for i in range(length,len(s)):
            check[s[i]] = check.get(s[i],0)+1
            left = s[i - length]
            check[left] -= 1
            if check[left] == 0:
                del check[left]
            if main == check:
                answer.append(i - length + 1)
        return answer