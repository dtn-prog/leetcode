class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        elements:dict[int:int] = {}
        for num in nums:
            if num in elements:
                return True
            elements[num] = 1
        return False
