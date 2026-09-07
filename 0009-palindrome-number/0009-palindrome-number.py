class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        res = 0

        while num>0:
            ld = num%10
            res = (res*10)+ ld
            num = num//10
        
        return res == x