class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        i = 0
        n = x
        while i < len(str(x)):
            ld = n%10
            res = (res*10)+ld
            n = n//10
            i+=1

        return x == res
        
        
        return str(res) == x