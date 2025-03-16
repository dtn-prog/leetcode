from icecream import ic

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}
        
        for c1, c2 in zip(s, t):
            ic(c1, c2)
            s_dict[c1] = s_dict.get(c1, 0) + 1
            t_dict[c2] = t_dict.get(c2, 0) + 1
        ic('loop done')
        return s_dict == t_dict

solution = Solution()

print(solution.isAnagram('racecar', 'carrace'))