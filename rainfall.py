# Part 1: Average Rainfall Calculation

# Ask for the number of years
num_years = int(input("Enter the number of years: "))

# Initialize total rainfall and month count
total_rainfall = 0
total_months = 0

# Outer loop iterates once for each year
for year in range(1, num_years + 1):
    print(f"Year {year}")

    # Inner loop iterates twelve times, once for each month
    for month in range(1, 13):
        rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
        total_rainfall += rainfall
        total_months += 1

# Calculate average rainfall
average_rainfall = total_rainfall / total_months

# Display results
print(f"\nTotal number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall}")
print(f"Average rainfall per month: {average_rainfall:.2f}")
