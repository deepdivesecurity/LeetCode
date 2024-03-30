class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0, 0)
        highestInt = 0
        
        for i in range(len(gain)): 
            if i == 0: 
                continue
            else: 
                gain[i] = gain[i] + gain[i-1]
                if gain[i] > highestInt: 
                    highestInt = gain[i]
        
        return highestInt
