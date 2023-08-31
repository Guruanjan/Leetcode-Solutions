class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i not in nums:
                return i
        if len(res) ==0:
            return nums[len(nums)-1] + 1