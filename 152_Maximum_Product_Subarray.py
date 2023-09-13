class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix , suffix , max_sofar = 0 , 0 , float('-inf')
        n = len(nums)
        for i in range(n):
            prefix = (prefix or 1 ) * nums[i]
            suffix = (suffix or 1 ) * nums[n-1-i]
            max_sofar = max(max_sofar , prefix , suffix)
        return max_sofar
        