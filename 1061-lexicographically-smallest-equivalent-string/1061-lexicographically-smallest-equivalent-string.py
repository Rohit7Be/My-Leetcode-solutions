class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(x):
            if parent[x] == x:
                return parent[x]
            parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            i = find(a)
            j = find(b)

            if i>j:
                parent[i] = j
            else:
                parent[j] = i

        for a,b in zip(s1,s2):
            x = ord(a) - ord('a')
            y = ord(b) - ord('a')
            union(x,y)

        res = []

        for ch in baseStr:
            x = ord(ch) - ord('a')
            root = find(x)
            res.append(chr(root + ord('a')))

        return ''.join(res)

