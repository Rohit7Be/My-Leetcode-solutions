class Solution:
    def compress(self, chars: list[str]) -> int:
        ans = 0 # pointer for placing the new letter
        i = 0 # pointer for traversing through the chars.

        while i<len(chars):
            letter = chars[i]
            c = 0
            while i<len(chars) and chars[i]== letter:
                c+=1
                i+=1
            chars[ans] = letter
            ans +=1
            if c>1:
                for n in str(c):
                    chars[ans] = n
                    ans+=1

        return ans