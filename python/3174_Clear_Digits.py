class Solution:
    def clearDigits(self, s: str) -> str:
        chars = []

        for c in s:
            if c.isdigit():
                chars.pop(-1)
            else:
                chars.append(c)

        return ''.join(chars)


print(Solution().clearDigits("a1b2c3"))  # "abc"
print(Solution().clearDigits("cb34"))  # ""
