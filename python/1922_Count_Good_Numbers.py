class Solution:
    def countGoodNumbers(self, n: int) -> int:
        res = 5
        i = 1
        MOD = 10 ** 9 + 7
        while i < n:
            if i % 2 == 0:
                res *= 5 % MOD
            else:
                res *= 4 % MOD
            i += 1

        return res % MOD


print(Solution().countGoodNumbers(4))
