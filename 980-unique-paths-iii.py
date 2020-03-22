from typing import List

class Solution:
    n: int #szerokosc
    m: int #wysokosc
    grid: List[List[int]]
    starti, startj, endi, endj = None, None, None, None

    def checkPath(self, curi, curj, vis, pathLength):
        if pathLength == 0 and (curi != self.starti or curj != self.startj):
            return 0

        if curi == self.starti and curj == self.startj:
            return 1

        vis[curi][curj] = True
        res = 0

        if curi > 0 and not vis[curi-1][curj] and self.grid[curi-1][curj] != -1:
            res += self.checkPath(curi-1, curj, vis, pathLength-1)

        if curi < self.m-1 and not vis[curi+1][curj] and self.grid[curi+1][curj] != -1:
            res += self.checkPath(curi + 1, curj, vis, pathLength - 1)

        if curj > 0 and not vis[curi][curj - 1] and self.grid[curi][curj - 1] != -1:
            res += self.checkPath(curi, curj - 1, vis, pathLength - 1)

        if curj < self.n-1 and not vis[curi][curj + 1] and self.grid[curi][curj+1] != -1:
            res += self.checkPath(curi, curj + 1, vis, pathLength - 1)

        return res


    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.n = len(grid[0])
        self.m = len(grid)
        self.grid = grid

        vis = [[0]*self.n for x in range(self.m)]
        emptySquaresCnt = 0

        for i in range(self.m):
            for j in range(self.n):
                vis[i][j] = False

                if grid[i][j] == 2:
                    self.endi = i
                    self.endj = j

                if grid[i][j] == 1:
                    self.starti = i
                    self.startj = j

                emptySquaresCnt += 1 if grid[i][j] == 0 else 0

        return self.checkPath(self.endi, self.endj, vis, emptySquaresCnt)




s = Solution()
print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
#print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
#print(s.uniquePathsIII([[0,1],[2,0]]))