class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        ops = 0

        # Sort the list
        nums.sort()

        while left < right: 
            # Check if the current left and right pointers are equal to k, if so, move them both and increment the number of operations by 1
            if nums[left] + nums[right] == k: 
                ops += 1
                left += 1
                right -= 1
            # Otherwise check if left and right are greater than K, if so, move the right pointer back
            elif nums[left] + nums[right] >= k: 
                right -= 1
            else: 
                left += 1
        
        return ops
