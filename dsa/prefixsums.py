class PrefixSums:
    def __init__(self, nums):
        self.prefixsums = []
        total = 0
        for n in nums:
            total += n
            self.prefixsums.append(total)