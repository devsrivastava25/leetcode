class Solution(object):
    # well weare tracking the elements which are not include in window 
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        total = sum(cardPoints)
        window_sum = sum(cardPoints[:n - k])   # size n-k
        minimum = window_sum

        for i in range(n - k, n):
            window_sum += cardPoints[i]
            window_sum -= cardPoints[i - (n - k)]
            minimum = min(minimum, window_sum)

        return total - minimum   