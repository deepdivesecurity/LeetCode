class Solution:
    def reverseVowels(self, s: str) -> str:
        # Initialize variables
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        right_ptr = -1
        swapped = ""

        # Loop through the string starting on the left side
        for i, char in enumerate(s): 
            # If the current char is a vowel, we need to swap it
            if char in vowels: 
                # Find the vowel to swap with by decreasing the right pointer
                while right_ptr != 0: 
                    if s[right_ptr] in vowels: 
                        swapped += s[right_ptr]
                        right_ptr -= 1
                        break
                    right_ptr -= 1
            else: 
                swapped += char

        return swapped
