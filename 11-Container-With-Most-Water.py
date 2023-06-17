class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max = 0
        l,r = 0 , n - 1 
        while l< r :
            temp = min(height[r] , height[l]) * abs(l-r)
            if max < temp:
                max = temp 
            if height[l] < height[r]:
                l+=1 
            else:
                r -=1 
        return max 