class Solution(object):
    def subarraysDivByK(self, nums, k):
        sum = 0            # running prefix sum
        rem = {0: 1}       # "before any element", prefix sum is 0, remainder is 0
        answer = 0         # our final count

        for num in nums:
            sum += num                 # extend the running sum
            r = sum % k                # what's the remainder?

            answer += rem.get(r, 0)    # how many PREVIOUS positions had this same remainder?
                                       # each one forms a valid subarray with current position

            rem[r] = rem.get(r, 0) + 1 # now record: "I've seen remainder r one more time"

        return answer   