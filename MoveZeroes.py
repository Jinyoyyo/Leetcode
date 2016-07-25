class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lastPos = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                for j in range(i, lastPos):
                    nums[j] = nums[j+1]
                nums[lastPos] = 0
                lastPos -= 1
    #1y, 464ms, beats 8.98% of pythonsubmissions.

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        zeros = i = 0
        while i + zeros < size:
            if nums[i + zeros] == 0:
                zeros += 1
            else:
                nums[i] = nums[i + zeros]
                i += 1
        for i in range(zeros):
            nums[size - 1 - i] = 0
    #6y, 72ms, beats 80.35% of pythonsubmissions.