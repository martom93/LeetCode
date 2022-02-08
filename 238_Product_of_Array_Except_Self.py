
class Solution(object):
    
    def productExceptSelf(self, nums):
        if not nums:
            return []

        left = [1 for _ in xrange(len(nums))]
        for i in xrange(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        right = 1
        for i in xrange(len(nums) - 2, -1, -1):
            right *= nums[i + 1]
            left[i] = left[i] * right

        return left