class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = 1
        output = [1]
        size = len(nums)
        for i in range(1, len(nums)):
            tmp *= nums[i-1]
            output.append(tmp)
        tmp = 1
        for i in range(1, len(nums)):
            tmp *= nums[len(nums)-i]
            output[len(nums)-1-i] *= tmp
        return output

#refer to discuss,4y,beats 59.14% of pythonsubmissions.
#len(list) is faster than save length as const??