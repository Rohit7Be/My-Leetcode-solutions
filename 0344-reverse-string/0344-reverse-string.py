class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # i will do it using recursion 
        # and i will use two pointers here 

        def func(s,L,R):
            if L>=R:
                return
        
            s[L], s[R] = s[R], s[L]
            func(s,L+1, R-1)

        func(s, 0, len(s)-1)
        

        