from icecream import ic

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # solution with division, if there are more than two 0, the output is
        # nothing but zero, if there is one zero the output is the product at the zero
        # index, if no zero, just divide like normal
        # product = 1
        # zero_c = 0
        # zero_at = -1
        # for i,n in enumerate(nums):
        #     if n != 0:
        #         product *= n
        #     else:
        #         zero_at = i
        #         zero_c += 1

        # output = []
        # if zero_c > 1:
        #     return [0] * len(nums)
        
        # if zero_c == 1:
        #     output = [0] * len(nums)
        #     output[zero_at] = product
        #     return output
        
        # for n in nums:
        #     output.append(int(product/n))
        
        # return output
        
        
        # using pre,post products
        # prod = PrePostfixproducts(nums)
        
        # output = []
        # for i,n in enumerate(nums):
        #     x = prod.getPrefix(i - 1) * prod.getPostfix(i + 1)
        #     print(x)
        #     output.append(x)
        # return output
        
        # a better way to use prefix, postfix, use the output arr
        # as prefix and postfix
        output = [1] * len(nums)
        
        prefix = 1
        for i,n in enumerate(nums):
            output[i] = prefix
            prefix *= n
        
        ic(output)
        size = len(nums)
        postfix = 1
        for i in range(size - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        ic(output)
        return output
        
    
class PrePostfixproducts:
    
    def __init__(self, nums):
        self.nums = nums
        self.prefixproducts = []
        self.postfixproducts = []
        products = 1
        for n in nums:
            products *= n
            self.prefixproducts.append(products)
            
        products = 1
        for n in reversed(nums):
            products *= n
            self.postfixproducts.append(products)

    def getPrefix(self,i:int):
        return self.prefixproducts[i] if i >= 0 else 1
    
    def getPostfix(self,i:int):
        j = len(self.nums) - 1 - i
        return self.postfixproducts[j] if j >= 0 else 1
    
so = Solution()
so.productExceptSelf([1,2,4,6])