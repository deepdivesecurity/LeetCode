class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = None
        second_smallest = None

        # Loop through all of the numbers
        for num in nums: 
            # Check if the initial numbers have been set
            if smallest == None: 
                smallest = num
                continue

            if second_smallest == None and num > smallest: 
                second_smallest = num
                continue

            # If the current number is less than the current smallest, then replace the current smallest
            if num <= smallest: 
                smallest = num
            # If the number is > than the smallest, but less than the second smallest, replace the second smallest
            elif num <= second_smallest: 
                second_smallest = num
            # If the number is neither of the above, then we can say it's the 3rd number in our triplet sequence
            else: 
                return True

        return False
