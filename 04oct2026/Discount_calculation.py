price = int(input("Enter the price: "))
discount = int(input("Enter the discount: "))

discount_amount = (discount/100)*price

print(f"discount amount: {discount_amount}")
print(f"final price: {price - discount_amount}")