year = 360
month = 30

days = int(input("Enter the Days: "))

total_year = days // year
total_months = (days % year) // month
remaining_days = (days % year) % month

print(f"Year: {total_year}, Months: {total_months}, Days: {remaining_days}")