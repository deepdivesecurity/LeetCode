class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        num_moves = 0

        # Sort the 2 lists
        students.sort()
        seats.sort()

        # Loop through the students, assigning each student to the lowest chair available
        for i in range(len(students)): 
            if students[i] >= seats[i]: 
                num_moves = num_moves + (students[i] - seats[i])
            else: 
                num_moves = num_moves + (seats[i] - students[i])
            
        return num_moves
