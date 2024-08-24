class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Variable to hold index that new element must be put into
        index = 0

        # Loop through each number in the list
        for i in range(len(nums)): 
            # If the number at the held index location is the same as the current loop, skip it
            if nums[index] == nums[i]: 
                continue
            else: 
                # If the number is different, then add the number to the held index spot + 1
                index += 1
                nums[index] = nums[i]

        # Return the index + 1 to account for index 0
        return index + 1
