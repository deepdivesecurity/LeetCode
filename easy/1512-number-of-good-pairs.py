from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Create a hashmap of the unique elements with their quantities
        di = Counter(nums)
        good_pairs = 0

        # Loop through the hashmap calculating the number of pairs that can be created from each element
        for key, value in di.items(): 
            good_pairs = good_pairs + (value * (value - 1) // 2)

        return good_pairs
