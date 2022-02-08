class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        szukane = {}
        for i in range(len(nums)):
            if nums[i] in szukane:
                return[szukane[nums[i]],i]
            else:
                szukane[target-nums[i]] = i
        return None
