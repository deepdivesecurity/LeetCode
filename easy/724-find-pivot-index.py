class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index = -1
        nums_length = len(nums)

        # Loop through each index in nums
        for i in range(len(nums)): 
            # Check if the sum left of i is equal to the sum right of i using slicing; if it is, return i
            if sum(nums[0:i]) == sum(nums[i+1:nums_length]): 
                return i
        
        return index
        
