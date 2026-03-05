# Darrin Sandoval
# March 3, 2026
# P1HW2 - Travel Budget Calculator
# This program asks the user for their travel budget and estimated expenses 
# (gas, accommodation, food), calculates the total expenses, and displays 
# how much money remains (or if they are over budget).

# ====================
# Pseudocode / Program Logic
# ====================
# 1. Display a welcome/title message
# 2. Ask user to enter their total budget (float)
# 3. Ask user to enter travel destination (string)
# 4. Ask user for gas expense (float)
# 5. Ask user for accommodation expense (float)
# 6. Ask user for food expense (float)
# 7. Calculate total expenses = gas + accommodation + food
# 8. Calculate remaining balance = budget - total expenses
# 9. Display formatted results:
#    - Travel destination
#    - Initial budget
#    - Each expense
#    - Total expenses
#    - Remaining balance (positive, negative, or zero)
# 10. Use clear formatting with $ and two decimal places

print("--- Travel Expense Calculator ---")
print()

# Get user inputs
budget = float(input("Enter your budget for the trip: $"))
destination = input("Enter your travel destination: ")
gas = float(input("How much will you spend on gas? $"))
accommodation = float(input("How much will you spend on accommodation? $"))
food = float(input("How much will you spend on food? $"))

# Calculations
total_expenses = gas + accommodation + food
remaining = budget - total_expenses

# Display results
print("\n------------Travel Expenses------------")
print(f"Location:          {destination}")
print(f"Initial Budget:    ${budget:,.2f}")
print(f"Gas:               ${gas:,.2f}")
print(f"Accommodation:     ${accommodation:,.2f}")
print(f"Food:              ${food:,.2f}")
print("---------------------------------------")
print(f"Total Expenses:    ${total_expenses:,.2f}")
print(f"Remaining Balance: ${remaining:,.2f}")

if remaining > 0:
    print("\nYou are under budget! Enjoy your trip!")
elif remaining == 0:
    print("\nYou have exactly used your budget.")
else:
    print("\nYou are OVER budget! Careful planning needed.")