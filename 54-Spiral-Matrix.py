class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix) # rows 
        n = len(matrix[0]) # columns 
        l, r, t, b = 0, n-1 , 0 , m-1
        res = []
        while l<=r and t<=b:
            for j in range(l,r+1,1):
                res.append(matrix[t][j])
            t+=1
            for j in range(t, b+ 1, 1):
                res.append(matrix[j][r])
            r -=1
            if len(res) == m *n:
                break
            for j in range(r,l -1, -1):
                res.append(matrix[b][j])
            b -=1
            for j in range(b, t-1, -1):
                res.append(matrix[j][l])
            l +=1
        return res 
            
                
                
        