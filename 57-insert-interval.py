from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        while intervals and intervals[0][1] < newInterval[0]:
            res.append(intervals.pop(0))
        overlapped = intervals.pop(0) if intervals and intervals[0][0] <= newInterval[1] else newInterval
        res.append([min(overlapped[0], newInterval[0]), max(overlapped[1], newInterval[1])])
        while intervals and res[-1][1] >= intervals[0][0]:
            res[-1][1] = max(intervals.pop(0)[1], newInterval[1])
        return res + intervals

def test(a, b):
    solution = Solution()
    return solution.insert(a,b)

assert test([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
assert test([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
assert test([[1,2]], [5,6]) == [[1,2],[5,6]]
assert test([[1,5]], [2,3]) == [[1,5]]
assert test([[1,5]], [0,0]) == [[0,0],[1,5]]