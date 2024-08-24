class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        
        # Loop through the list of operations determining the effect on value
        for op in operations: 
            match op: 
                case "--X": 
                    value -= 1
                case "X--": 
                    value -= 1
                case "++X": 
                    value += 1
                case "X++": 
                    value += 1
        return value
