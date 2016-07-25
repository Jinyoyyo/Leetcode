class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num % 9 if num % 9 > 0 else min(9, num)

#5y, 64ms, beats 69.36% of pythonsubmissions.
# =.=!