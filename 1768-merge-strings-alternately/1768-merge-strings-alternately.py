class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lenr = max(len(word1), len(word2))

        res = []

        for i in range(lenr):
            if i < len(word1) or i > len(word2):
                res.append(word1[i])
                if i < len(word2):
                    res.append(word2[i])
            else:
                res.append(word2[i])
                if i < len(word1):
                    res.append(word1[i])

        return "".join(res)
