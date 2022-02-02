class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for key, value in enumerate(nums):
            remainder = target - value
            
            if remainder in seen:
                return [key, seen[remainder]]
            
            seen[value] = key
