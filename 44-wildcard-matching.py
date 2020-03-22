class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        matching = [[0]*len(p) for x in range(len(s))]
        matching[0][0] = True

        for j in range(1, len(p)):
            matching[0][j - 1] = p[j - 1] == "*"

        for i in range(len(s)):
            matching[i][0] = len(p) == 0

        print(matching)
        #return matching[len(s)-1][len(p)-1]


s = Solution()
s.isMatch("aa", "*")
s.isMatch("cb", "?b")