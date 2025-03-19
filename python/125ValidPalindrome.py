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

def is_alphanumeric(char: str):
    if char >= ord('a') and ord(char) <= ord('z'):
        return True
    if char >= ord('A') and ord(char) <= ord('Z'):
        return True
    if char >= ord('1') and ord(char) <= ord('9'):
        return True
    return False