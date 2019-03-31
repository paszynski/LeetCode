from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        t = {}
        for i in range(n):
            if target - nums[i] in t.keys():
                return [t[target - nums[i]], i]
            else:
                t[nums[i]] = i
        return [None, None]


s = Solution()
print(s.twoSum([2, 7, 11, 15], 20))
