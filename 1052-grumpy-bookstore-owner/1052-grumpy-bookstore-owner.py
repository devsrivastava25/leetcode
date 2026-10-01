class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        # Base: already satisfied (non-grumpy) customers
        base = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)

        # Extra: grumpy customers saved by the patience window
        window_sum = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
        max_extra = window_sum

        for r in range(minutes, len(customers)):
            if grumpy[r] == 1:
                window_sum += customers[r]
            if grumpy[r - minutes] == 1:
                window_sum -= customers[r - minutes]
            max_extra = max(max_extra, window_sum)

        return base + max_extra   