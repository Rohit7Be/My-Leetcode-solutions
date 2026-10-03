class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = n

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:

                emptyL = (i == 0) or (flowerbed[i-1]== 0)

                emptyR = (i == len(flowerbed)-1) or (flowerbed[i+1] ==0)

                if emptyL and emptyR:
                    flowerbed[i] = 1
                    count -=1
                    
            
        return count<=0