class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largestCandie = 0
        result = [False for n in range(len(candies))]

        for i in candies: 
            if i > largestCandie: 
                largestCandie = i

        for y in range(len(candies)): 
            if candies[y] + extraCandies >= largestCandie: 
                result[y] = True
            else: 
                result[y] = False
                        
        return result
