class Solution:
    def maxArea(self, height: List[int]) -> int:
        curr_max = 0
        left = 0
        right = len(height) - 1

        while left < right: 
            # Length = (right - left) # This is the length of the array
            # Height = min(height[left], height[right])
                # Have to use min because water would spill over otherwise
            # Compare the current max height against the new max height to keep the larger
            curr_max = max(curr_max, (right - left) * min(height[left], height[right]))

            # Iterate the smaller height and keep the larger height
            if height[left] < height[right]: 
                left += 1
            else: 
                right -= 1

        return curr_max
