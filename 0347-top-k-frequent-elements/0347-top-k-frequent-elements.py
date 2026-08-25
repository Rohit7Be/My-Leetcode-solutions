class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = {n : nums.count(n) for n in set(nums)}
        maxF = sorted(dic.keys(), key=lambda x: (dic[x], x), reverse=True)

        return maxF[:k]