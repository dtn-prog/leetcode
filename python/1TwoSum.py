class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}
        
        for i, num in enumerate(nums):
            to_find_val = target - num
            if to_find_val not in prevMap:
                prevMap[num] = i
                print(prevMap)
            else:
                return [prevMap[to_find_val], i]
        
        return []

solution = Solution()

print(solution.twoSum(nums = [3,4,5,6], target = 7))