class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Remove duplicates and sort the list
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            target = - nums[i]
            l = i+ 1 
            r = n - 1
            if nums[i] == nums[i-1] and i>0:
                continue 
            while l<r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l] ==nums[l-1] and l < r:
                        l+=1  
                elif nums[l] + nums[r] > target:
                    r -=1 
                else:
                    l+=1
        return res 

