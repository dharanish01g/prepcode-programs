class Solution:
    def isDivisible(self, a: int, b: int) -> bool:
        if b == 0:
            return False
        if a % b == 0:
            return True
        else:
            return False
        
