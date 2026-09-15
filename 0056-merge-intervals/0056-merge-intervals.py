class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = [intervals[0]]
        for curr in intervals[1:]:
            last = res[-1]

            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                res.append(curr)

        return res