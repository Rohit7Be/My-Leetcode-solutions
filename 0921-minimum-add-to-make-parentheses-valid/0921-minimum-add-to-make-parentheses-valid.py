class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openB  = 0
        minAdd = 0

        for i in s:
            if i == "(":
                openB +=1
            else:
                if openB > 0:
                    openB -=1
                else:
                    minAdd +=1

        return minAdd + openB 