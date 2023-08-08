class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #bool flag= false
        l= len(nums)
        nums.sort()
        if l==1:
            return False
        if l>=1 or l<=100000:
            for i in range(0,l-1):
                k= nums[i]
                if k>=-1000000000 or k<=1000000000:
                        if k == nums[i+1]:
                            return True
        return False