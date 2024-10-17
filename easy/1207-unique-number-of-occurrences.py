class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_hash = {}
        values = []

        # Loop through list adding numbers to the hashmap w/ their number of occurrences - O(1)
        for num in arr: 
            if num not in arr_hash: 
                arr_hash[num] = 1
            else: 
                arr_hash[num] += 1

        # Check if any values in the hashmap are repeated
        for key, value in arr_hash.items(): 
            if value in values: 
                return False
            else: 
                values.append(value)
        
        return True
