class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Declare variables
        longest = 0

        # Get a set of the list of nums
        nums_set = set(nums)

        # Go through each element and see if it's the start of a sequence by checking if it's left neighbour exists (e.g. given 4, does 3 exist? If 3 exists, 4 is not the start)
        for element in nums_set: 
            # Check if start of sequence
            if (element - 1) not in nums_set: 
                seq_length = 1
                # Loop through until there are no more elements above this
                while (element + seq_length) in nums_set: 
                    seq_length += 1
                # Check if this sequence length is greater than our longest
                if seq_length > longest: 
                    longest = seq_length
                
                # Reset seq_length
                seq_length = 0
        return longest
