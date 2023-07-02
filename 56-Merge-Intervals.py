class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the array wrt first element
        intervals.sort()
        # Edge cases
        if len(intervals) == 1 or len(intervals) ==0:
            return intervals
        
        # merge overlapping intervals
        i  = 1
        while i < len(intervals):
            c_start = intervals[i][0]
            p_start = intervals[i-1][0]
            p_end = intervals[i-1][1]
            if c_start <= p_end and c_start>= p_start:
                if intervals[i-1][1] < intervals[i][1]:
                    intervals[i-1][1] = intervals[i][1]
                intervals.pop(i)
            else:
                i+=1 
        return intervals 