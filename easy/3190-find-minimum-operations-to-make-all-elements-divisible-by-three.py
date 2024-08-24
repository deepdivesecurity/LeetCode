class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0

        # Loop through each number checking to see % 3 results
        for number in nums: 
            # If the result of % 3 is 0, continue to the next number because no operation is needed
            if number % 3 == 0: 
                continue
            # If the result of % 3 is not 0, then it requires an operation
            elif (number + 1) % 3 == 0 or (number - 1) % 3 == 0: 
                operations += 1
                
        return operations
