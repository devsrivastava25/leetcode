from collections import deque

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(sr, sc, grid, vis):
            vis[sr][sc] = 1
            q = deque()
            q.append([sr, sc])
            area = 0
            while q:
                cr, cc = q.popleft()
                area += 1
                for d in [[0,-1],[0,1],[-1,0],[1,0]]:
                    nr = cr + d[0]
                    nc = cc + d[1]
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1 and vis[nr][nc] == 0:
                        q.append([nr, nc])
                        vis[nr][nc] = 1
            return area

        maxarea = 0
        n, m = len(grid), len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    maxarea = max(maxarea, bfs(i, j, grid, vis))
        return maxarea   