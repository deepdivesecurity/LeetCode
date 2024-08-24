class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        to_return = []

        # Split the list of ints at n
        nums1 = nums[0:n]
        nums2 = nums[n:]

        # Loop through the total count of chars, alternating adding ints to new list
        for i in range(len(nums) // 2): 
            to_return.append(nums1[i])
            to_return.append(nums2[i])

        return to_return
