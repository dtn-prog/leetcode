from icecream import ic

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        sequence_starts = []
        for n in nums_set:
            if n - 1 not in nums:
                sequence_starts.append(n)
        ic(sequence_starts)
        result = 0
        for n in sequence_starts:
            i = 1
            while True:
                if (n+1) in nums_set:
                    i += 1
                    n+=1
                else:
                    break
            if result < i:
                result = i
        return result
so = Solution()
result = so.longestConsecutive([2,20,4,10,3,4,5])
ic(result)
