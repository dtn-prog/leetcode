from collections import defaultdict
from icecream import ic

def get_alphabet_ordinal(char:str):
    return ord(char) - ord('a')

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) <= 1:
            return [strs]
        
        my_dict = defaultdict(list)
        
        for str in strs:
            alphabet = [0]*26
            for char in str:
                ordinal = get_alphabet_ordinal(char)
                alphabet[ordinal]+=1
            ic(alphabet, str)
            my_dict[tuple(alphabet)].append(str)
        
        return list(my_dict.values())
        
    
solution = Solution()
print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]))