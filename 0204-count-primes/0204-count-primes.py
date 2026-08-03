class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=2: #anything under this is not a prime
            return 0

        prime = [True]*n #creating a list of true, making all the vals true(prime)
        prime[0] = False  #0 is not prime
        prime[1] = False #1 is also not prime

        p = 2 #starting the loop with 2

        while p*p < n: #start to check the multiple of 2. is it under the n or not
            if prime[p]: #if prime[p] is true

                for multiple in range(p*p, n, p): #checking the multiple under the range of n
                    prime[multiple] = False #setting all of them to False, because they are multiple 
            
            p+=1 #increment

        return sum(prime) #returning the sum of, how many true are in the list