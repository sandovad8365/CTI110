# Darrin Sandoval
# March 29, 2026
# P3LAB - Making Change
# This program takes a float dollar amount and breaks it down into the 
# smallest number of dollars, quarters, dimes, nickels, and pennies.

# Get input from user
amount = float(input("Enter the amount of money: $"))

# Convert to cents to avoid floating point issues
cents = int(amount * 100)

# Calculate each coin type using integer division
dollars = cents // 100
cents = cents % 100

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
cents = cents % 5

pennies = cents

# Display results - only show coins that are needed
print()

if dollars > 0:
    print(f"{dollars} dollar{'s' if dollars > 1 else ''}")

if quarters > 0:
    print(f"{quarters} quarter{'s' if quarters > 1 else ''}")

if dimes > 0:
    print(f"{dimes} dime{'s' if dimes > 1 else ''}")

if nickels > 0:
    print(f"{nickels} nickel{'s' if nickels > 1 else ''}")

if pennies > 0:
    print(f"{pennies} penn{'y' if pennies == 1 else 'ies'}")