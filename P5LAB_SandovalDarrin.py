# Darrin Sandoval
# April 27, 2026
# P5LAB
# This program simulates a self-checkout machine. It generates a random total,
# accepts cash from the user, calculates change, and uses a function to
# disperse the change in dollars and coins.

import random

def disperse_change(change):
    """Takes the change amount and prints the number of dollars and coins needed."""
    if change <= 0:
        print("No change due.")
        return

    # Convert to cents to avoid floating point issues
    cents = int(round(change * 100))

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    pennies = cents % 5

    # Print results (only show what is needed)
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'y' if pennies == 1 else 'ies'}")


def main():
    # Generate random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${total_owed:.2f}")

    # Get cash from user
    cash_given = float(input("Enter the amount of cash you are putting in: $"))

    # Calculate change
    change = cash_given - total_owed

    if change < 0:
        print("Insufficient cash. Transaction cancelled.")
    else:
        print(f"Change due: ${change:.2f}")
        disperse_change(change)


# Call the main function
if __name__ == "__main__":
    main()