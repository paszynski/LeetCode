from typing import List

class Solution:
    def findMedianSortedArraysLinear(self, A: List[int], B: List[int]) -> float:
        curr = prev = 0
        total = len(A) + len(B)
        nums = A + list(reversed(B))
        while total - len(nums) < (1 + int(total / 2)):
            index = -1 if nums[0] > nums[-1] else 0
            prev, curr = curr, nums.pop(index)
        return curr if total % 2 else (prev + curr) / 2.0

    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left / 1.0

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0


s = Solution()
print(s.findMedianSortedArrays([1, 2], [3, 4]))
print(s.findMedianSortedArrays([1, 3], [2]))
