class Solution:
    #不借助任何Python库的方案
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = -1
        secMax = -1
        idx = -1
        for n in range(len(nums)):
            if nums[n] > max:
                secMax = max
                max = nums[n]
                idx = n
            elif nums[n] > secMax:
                secMax = nums[n]
        if max >= secMax*2:
            return idx
        else:
            return -1
    
    #使用Python库的方案
    def dominantIndex2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        for n in nums:
            if 2*n > m and n != m:
                return -1
        return nums.index(m)
