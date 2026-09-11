class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))
        res = []

        def find(x):
            if parent[x] == x:
                return parent[x]
            parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            i = find(a)
            j = find(b)

            if i>j:
                parent[i] = parent[j]
            else:
                parent[j] = parent[i]


        for a,b in zip(s1,s2):
            x = ord(a) - ord('a')
            y = ord(b) - ord('a')
            union(x,y)

        for ch in baseStr:
            root = find(ord(ch) - ord('a'))
            res.append(chr(root + ord('a')))

        return "".join(res) 

        