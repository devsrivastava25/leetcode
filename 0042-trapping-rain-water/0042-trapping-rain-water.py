class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        Lmax=0
        Rmax = 0
        ans = 0
        left = 0
        right = len(height)-1
        while left<right:
            Lmax = max(Lmax,height[left])
            Rmax = max(Rmax,height[right])

            if Lmax < Rmax:
                ans +=(Lmax-height[left])
                left += 1
            else:
                ans += (Rmax-height[right])
                right -= 1
                
        return ans
