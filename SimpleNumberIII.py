class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        check0 = 0
        check1 = 0
        for i in nums:
            check0 ^= i
            check1 ^= -i
            nums_set.add(i)
        for i in nums:
            tmp = check0 ^ i
            if tmp == -(check1 ^ (-i)) and tmp in nums:
                return [i, tmp]
	#1y, 624ms, beats 4.97% of pythonsubmissions.

	def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        check0 = 0
        check1 = 0
        nums_set = set()
        for i in nums:
            check0 ^= i
            check1 ^= -i
            nums_set.add(i)
        for i in nums:
            tmp = check0 ^ i
            if tmp == -(check1 ^ (-i)) and tmp in nums_set:
                return [i, tmp]
	#2y, O(NlogN) 56ms, beats 63.18% of pythonsubmissions.

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        checkSum = 0
        lastDiff = 0
        for i in nums:
            checkSum ^= i
        lastDiff = (checkSum & (checkSum - 1)) ^ checkSum # shenzhiyishou
        a = b = 0
        for i in nums:
            if i & lastDiff:
                a ^= i
            else:
                b ^= i
        return [a, b]
    #refer to @lchen77, O(N) 52ms, beats 80.35% of pythonsubmissions.