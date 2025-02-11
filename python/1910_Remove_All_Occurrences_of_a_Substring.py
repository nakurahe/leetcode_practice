class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if part not in s:
            return s

        s = s.replace(part, "")

        return self.removeOccurrences(s, part, 1)


print(Solution().removeOccurrences("aabababa", "aba"))  # "ba"
