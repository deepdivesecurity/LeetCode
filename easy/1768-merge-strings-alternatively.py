class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize variables
        new_word = ""
        i = 0
        word1_len = len(word1)
        word2_len = len(word2)

        # Loop through the length of the words
        while (i < word1_len or i < word2_len): 
            # If the pointer is less than the length of word1, append another char from word1
            if i < word1_len: 
                new_word += word1[i]
            
            # If the pointer is less than the length of word2, append another char from word2
            if i < word2_len: 
                new_word += word2[i]
            
            i += 1

        return new_word
