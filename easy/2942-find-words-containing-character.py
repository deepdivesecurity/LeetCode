class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices = []
        
        # Loop through each word in the list maintaining a list of elements which contain the char
        for i in range(len(words)): 
            # Check if the current word has the char and append to indices list if it does
            if words[i].find(x) != -1: 
                indices.append(i)

        return indices
        
