class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        num = 0
        for x in range(len(nums)):
            num += nums[x]
            ans.append(num)
        return ans
