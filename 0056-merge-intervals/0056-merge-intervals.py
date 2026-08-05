class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() #first sort whole 

        res = []
        res.append(intervals[0]) #append first elem. from intervals

        for i in intervals:
            last = res[-1] #last res ka
            current = i #current abhi wale i ka

            if current[0] <= last[1]: #if this happens, mtlb overlap hai
                start = min(current[0] , last[0]) #start min hoga dono ke first ka
                end = max(current[1] , last[1]) #end max hoga dono ke last ka 
                res.pop() #last wala elem delete kyuki ye wala ayega 
                res.append([start,end]) #iss wale ko add 
            else:
                res.append(i) 

        return res