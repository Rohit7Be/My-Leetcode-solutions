class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        c = 0
    
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:

                empL = (i == 0) or (flowerbed[i-1] == 0)
                   
                empR = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
        
                if empR and empL:
                    c+=1
                    flowerbed[i] = 1
            

        return c>=n        
