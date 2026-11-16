class Solution(object):
    def shipWithinDays(self, weights, days):
        
        def can(cap):
            d = 1
            current = 0
            for w in weights:
                if current + w > cap:
                    d += 1
                    current = w
                else:
                    current += w
            return d <= days

        lo = max(weights)
        hi = sum(weights)

        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo   