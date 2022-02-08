
class Solution(object):
    
    def productExceptSelf(self, nums):
        if not nums:
            return []

        left = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        right = 1
        for i in range(len(nums) - 2, -1, -1):
            right *= nums[i + 1]
            left[i] = left[i] * right

        return left