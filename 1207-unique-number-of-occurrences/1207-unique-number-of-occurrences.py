class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hashMap = dict()
        n = len(arr)
        for i in range(n):
            hashMap[arr[i]] = hashMap.get(arr[i],0)+ 1
 
        return len(set(hashMap.values())) == len(hashMap)
