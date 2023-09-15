class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n +1)
        def rec(nums, i):
            if i < 0 :
                return 0 
            if dp[i]>=0 :
                return dp[i]
            res= max( nums[i] + rec(nums, i - 2 ), rec(nums, i - 1 ))
            dp[i] = res
            return dp[i]
        a = rec(nums, n-1)
        return a
        
        