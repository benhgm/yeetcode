class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for key, value in enumerate(nums):
            remainder = target - value
            if remainder in nums[key+1:]:
                return [key, nums[key+1:].index(remainder) + key+1]
