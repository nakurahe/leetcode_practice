class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_q = []
        d_q = []
        next_i = len(senate)

        for i, char in enumerate(senate):
            if char == 'R':
                r_q.append(i)
            else:
                d_q.append(i)

        while r_q and d_q:
            curr_r = r_q.pop(0)
            curr_d = d_q.pop(0)
            if curr_r < curr_d:
                r_q.append(next_i)
            else:
                d_q.append(next_i)
            next_i += 1

        return "Radiant" if r_q else "Dire"


print(Solution().predictPartyVictory("RRDDD"))  # Radiant
