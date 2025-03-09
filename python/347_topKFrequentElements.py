from icecream import ic

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        size = len(nums) + 1
        freqs = [[] for _ in range(size)]
        freqMap = {}
        
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        for key, value in freqMap.items():
            freqs[value].append(key)
        
        ic(freqMap)
        ic(freqs)
        output = []
        for n in reversed(freqs):
            for i in n:
                output.append(i)
                k-=1
                if k <= 0:
                    return output
        return output
        ic(output)
        
solution = Solution()

solution.topKFrequent([7,7], 1)