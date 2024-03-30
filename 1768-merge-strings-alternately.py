class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0
        if len(word1) <= len(word2): 
            while i < len(word1): 
                result = result + word1[i]
                result = result + word2[i]
                i += 1
            result = result + word2[i:len(word2)]
        else: 
            while i < len(word2): 
                result = result + (word1[i])
                result = result + (word2[i])
                i += 1
            result = result + word1[i:len(word1)]
        return result
