class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        totalContainer = n*n
        noContainer = maxWeight//w
        answer = 0
        if noContainer>totalContainer:
            answer = totalContainer
        else:
            answer = noContainer
        return answer