total_amount = int(input("Enter the Total Price: "))
if total_amount > 1000:
    print(f"Final price: {total_amount - total_amount * 0.1}")
else:
    print(f"Final price: {total_amount}")