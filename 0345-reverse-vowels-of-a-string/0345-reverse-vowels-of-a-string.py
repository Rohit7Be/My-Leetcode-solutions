class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        lVowels = list(vowels)
        addV = []
        for i in s:
            if i in lVowels:
                addV.append(i)
        
        slist = list(s)
        for i in range(len(slist)):
            if slist[i] in lVowels:
                slist[i] = addV.pop()
        
        return "".join(slist)
        
