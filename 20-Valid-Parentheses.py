class Solution:
     def isValid(self, s: str) -> bool:
            stack =[]
         # will add open brackets to stack and pop open brackets if closed bracket encountered 
            hashmap={'(':0, ')':1, '{':0, '}':1, '[':0 , ']':1} # bracket value, open - 0 and closed - 1
            otc = {')':'(', '}': '{', ']': '['}
            i = 0
            n = len(s)
            if len(s) %2 != 0 or hashmap[s[0]] == 1:
                return False
            while i< n:
                if hashmap[s[i]] == 0:# open bracket
                    stack.append(s[i])
                else:# closed bracket 
                    if len(stack) ==0:
                        return False
                    a= stack.pop()
                    if a != otc[s[i]]:
                        return False
                i +=1
            if len(stack) ==0:
                return True 
