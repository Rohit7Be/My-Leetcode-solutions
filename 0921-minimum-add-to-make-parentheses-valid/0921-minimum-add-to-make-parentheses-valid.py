class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openBrac = 0
        minAddBrac = 0

        for i in s:
            if i == "(":
                openBrac += 1
            else:
                if openBrac > 0:
                    openBrac -=1
                else:
                    minAddBrac +=  1
        return openBrac + minAddBrac