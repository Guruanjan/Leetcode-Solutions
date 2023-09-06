class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {} # nums - freq
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 1
            else:
                map[nums[i]] += 1
        #map = {1: 3 , 2: 2 , 3: 3} -> {2:[2], 3:[1,3]}
        freq = [[] for i in range(len(nums)+ 1)]
        for n , c in map.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        