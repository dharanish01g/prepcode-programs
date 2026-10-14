class Solution:
    def computeShoppingBill(self, itemPrices: list[int]) -> int:
        total = 0
        for i in itemPrices:
            total = total + i
        return total
        
