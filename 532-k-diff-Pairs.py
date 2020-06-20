from typing import List

class Solution:
    lookup = dict()
    existed = dict() # lower value of pair
    
    def tryAddPair(self, a, b):
        if not self.existed.get(min(a,b), False) and self.lookup.get(b, 0) > 0:
            self.existed[min(a,b)] = True
            return 1
        else:
            return 0
    
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        self.lookup = dict()
        self.existed = dict()
        res = 0
        for num in nums:            
            res += self.tryAddPair(num, num - k) + self.tryAddPair(num, num + k)
            self.lookup[num] = self.lookup.get(num, 0) + 1
        return res

solution = Solution()
print(solution.findPairs([1,2,3,4,5], 5), 'vs', 0)
print(solution.findPairs([2,10,6], 4), 'vs', 2)
print(solution.findPairs([-1,-2,-3], 1), 'vs', 2)