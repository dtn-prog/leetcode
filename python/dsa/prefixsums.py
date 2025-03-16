# giố ng như prefixsum ta cũng có postfixsum bắ t đầ u từ cuối,
# còn có prefixproducts và postfixproducts, product ở đây là tích, phép nhân

class PrefixSums:
    def __init__(self, nums):
        self.prefixsums = []
        total = 0
        for n in nums:
            total += n
            self.prefixsums.append(total)