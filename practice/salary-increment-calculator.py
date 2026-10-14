class Solution:
    def calculateSalaryIncrement(self, currentSalary: int, score: int) -> int:
        # Write your code here
        if score >= 8:
            return int(currentSalary + (0.15 * currentSalary))
        elif score > 5 and score <= 7:
            return int(currentSalary + (0.10 * currentSalary))
        else:
            return int(cu
        )