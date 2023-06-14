class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Linear time complexity solution
        test = ""
        max_length = -1
        if (len(s) == 0) :
            return 0 
        elif (len(s) == 1):
            return 1 
        for c in list(s):
            current = "".join(c)
            if current in test:
                test = test[test.index(current) + 1: ]
            test = test + "".join(c)
            max_length = max(len(test), max_length)
        return max_length
        


     
