class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        visited = set()
        def dfs(i, j, m, n):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if matrix[i][j] == 0:
                visited.add(i)
                visited.add(j)
                matrix[i][j] = 0
                dfs(i-1, j, m, n)
                dfs(i+1, j, m, n)
                dfs(i, j-1, m, n)
                dfs(i, j+1, m, n)
            else:
                if i in visited:
                    dfs(i-1, j, m, n)
                    dfs(i+1, j, m, n)
                if j in visited:
                    dfs(i, j-1, m, n)
                    dfs(i, j+1, m, n)

        dfs(0,0,m,n)


print(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
