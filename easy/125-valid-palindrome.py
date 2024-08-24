class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a reversed version of s
        reversed_string = s[::-1]
        
        # Loop through getting rid of any special chars
        for char in [" ", "?",".",",","'", ":", "@", "#", "_", "{", "}", "\\", "[", "]", "\"", "-", ";", "<", ">", "*", "^", "&", "!", "(", ")", "`", "~"]: 
            s = s.replace(char, "")
            reversed_string = reversed_string.replace(char, "")

        # Compare strings and return result
        if (s.lower() == reversed_string.lower()): 
            return True
        else: 
            return False
