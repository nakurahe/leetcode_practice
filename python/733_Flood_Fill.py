class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image

        old_color = image[sr][sc]
        self.dfs(image, sr, sc, color, old_color)

        return image

    def dfs(self, image, i, j, color, old_color):
        if i in range(len(image)) and j in range(len(image[0])) and image[i][j] == old_color:
            image[i][j] = color
            self.dfs(image, i-1, j, color, old_color)
            self.dfs(image, i+1, j, color, old_color)
            self.dfs(image, i, j-1, color, old_color)
            self.dfs(image, i, j+1, color, old_color)
        else:
            return


print(Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))  # [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
