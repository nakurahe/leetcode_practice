import collections

def minWindow(s: str, t: str) -> str:
    char_cnt = collections.Counter(t)
    window = {}
    start, end = 0, 0
    res_len = float('inf')
    have, need = 0, len(char_cnt)
    l = 0

    for r in range(len(s)):
        if s[r] in char_cnt:
            window[s[r]] = 1 + window.get(s[r], 0)
            if window[s[r]] == char_cnt[s[r]]:
                have += 1

        while have == need:
            if r-l+1 < res_len:
                start, end = l, r
                res_len = r-l+1

            window[s[l]] -= 1
            if window[s[l]] < char_cnt[s[l]]:
                have -= 1
            l += 1
            while l < len(s) and s[l] not in char_cnt:
                l += 1

    return s[start:end+1] if res_len != float('inf') else ''


print(minWindow("ADOBECODEBANC", "ABC"))
