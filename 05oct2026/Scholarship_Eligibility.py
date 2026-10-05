percent = int(input("Enter the Percentage: "))
attendance = int(input("Enter the attendance: "))

if percent > 85 and attendance > 75:
    print("Scholarship eligible")
else:
    print("Not eligible")