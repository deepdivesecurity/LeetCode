class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_vowels = 0
        count = 0
        prev_char = ''
        first = True

        # Check if the window size is outside the bounds of the string
        if k > len(s): 
            return -1

        for i in range(len(s) - k + 1): 
            # Get the window
            window = s[i:k+i]

            # If first loop through, get the starting count of vowels and set the prev_char
            if first == True: 
                # Set prev_char
                prev_char = window[0]
                # Count vowels to get a starting point
                for j in window: 
                    if j in vowels: 
                        count += 1
                    max_vowels = count
                first = False
                continue

            # After the first loop, only care about the prev char and the next char for counting vowels
            # Check if the previous char of the window is a vowel, if it is, subtract 1 from the count
            if prev_char in vowels: 
                count -= 1
            
            # Check if the last char of the window is a vowel, if it is, add 1 to the count
            if window[k-1] in vowels: 
                count += 1
            
            # Set the previous char for the next round to the first char of the window
            prev_char = window[0]

            # Get the max between the current count vs. the max vowels we've found prior
            max_vowels = max(max_vowels, count)

            # Older solution - this worked, but wasn't time efficient
            #for j in window: 
            #    if j in vowels: 
            #        count += 1
            #if count > max_vowels: 
            #    max_vowels = count
            #count = 0

        return max_vowels
