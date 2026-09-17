class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """ done using DNF dutch national flag can be done using counting sort too but its time complexity would be logn + k"""
        low,mid = 0,0
       
        high = len(nums)-1

        while mid <= high:
         if nums[mid] == 0:
            nums[low],nums[mid] = nums[mid],nums[low]
            low += 1
            mid += 1
         elif nums[mid] == 1 :
            mid += 1
         else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high -= 1
