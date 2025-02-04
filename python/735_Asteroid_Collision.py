from collections import deque


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right_ast = deque([])
        left_ast = deque([])

        for ast in asteroids:
            if ast > 0:
                right_ast.append(ast)
            else:
                while right_ast and abs(right_ast[-1]) < abs(ast):
                    right_ast.pop()
                if not right_ast:
                    left_ast.append(ast)
                elif abs(right_ast[-1]) == abs(ast):
                    right_ast.pop()
        
        return list(left_ast) + list(right_ast)


print(Solution().asteroidCollision([5, 10, -5]))  # [5, 10]
