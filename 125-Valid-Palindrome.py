class Solution:
     def isPalindrome(self, s: str) -> bool:
         string = ""
         s = s.lower()
         for i in s:
             if i.isalpha() or i.isnumeric():
                 string += i
         print(string)
         print("".join(reversed(string)))
         if string == "".join(reversed(string)):
             return True
         else:
             return False