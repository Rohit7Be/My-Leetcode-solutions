class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        res = 0

        while n>0:
            ld = n%10
            res = (res*10) + ld
            n = n//10
        
        return res == x