class Solution:
    def computeFestivalDiscount(self, purchaseAmount: int, isGoldMember: bool) -> int:
        # Write your code here
        if isGoldMember and purchaseAmount >= 5000:
            return int(purchaseAmount * 0.20)
        elif isGoldMember and purchaseAmount < 5000:
            return int(purchaseAmount * 0.15)
        else:
            return int(purchaseAmount * 0.05)
