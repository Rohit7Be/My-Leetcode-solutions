class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        res = 0

        for c in s:
            if c in q:
                while q.popleft() != c:
                    continue
            q.append(c)
            res = max(res, len(q))
        return res