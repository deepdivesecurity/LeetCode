class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        to_return = []

        # Loop through the length of the array and append the appropriate int to the return array
        for i in range(len(nums)): 
            to_return.append(nums[nums[i]])

        return to_return
            
