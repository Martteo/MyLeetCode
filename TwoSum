class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = {}
        for i in range(len(nums)):
            if nums[i] in temp:
                return [temp[nums[i]], i]
            else:
                temp[target-nums[i]] = i
