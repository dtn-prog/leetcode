from icecream import ic
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while not s[i].isalnum() and i < j:
                i+=1
                continue
            while not s[j].isalnum() and i < j:
                j-=1
                continue
            
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True
        
so = Solution()
ic(so.isPalindrome('tab a cat'))