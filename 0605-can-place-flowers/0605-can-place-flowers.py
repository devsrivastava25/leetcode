class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed = [0] + flowerbed + [0]          # ← ADD: pad to avoid index errors

        for i in range(1, len(flowerbed) - 1):      # ← CHANGE: shifted range
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:  # ← FIX: check == 0, not truthy
                flowerbed[i] = 1                     # ← ADD: mark as occupied
                n -= 1
                if n <= 0:                           # ← ADD: early exit
                    return True
        return n <= 0   