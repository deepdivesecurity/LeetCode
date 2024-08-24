class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        emp_count = 0

        # Loop through the hours for each employee
        for num in hours: 
            # If the hours worked >= target, add to employee count
            if num >= target: 
                emp_count += 1

        return emp_count
