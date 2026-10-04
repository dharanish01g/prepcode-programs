number_of_items = int(input("Enter the Products count: "))
products_count_per_box = int(input("Enter the Box size/box: "))

total_box_needed = number_of_items // products_count_per_box
remaining_items = number_of_items % products_count_per_box

print(f"Total boxes needed {total_box_needed} and remaining items: {remaining_items}")