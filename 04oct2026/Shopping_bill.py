notebook_price = 45
pen_price = 20

notebook_count = int(input("Enter the Notebook count: "))
pen_count = int(input("Enter Pen count: "))

notebook_price = (notebook_count * notebook_price)
pen_price = (pen_count * pen_price)

print(f"Total is: {notebook_price + pen_price}")